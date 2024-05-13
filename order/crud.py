from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from order import models
from order import schemas
from order import utils as stripe_utils

async def create_order(order_data: schemas.OrderCreate, session):
    stripe_data = await stripe_utils.create_checkout_session(order_data)
    new_order = models.Order(
        product_id=order_data.product_id,
        product_quantity=order_data.product_quantity,
        user_id=order_data.user_id,
        product_total=order_data.product_total,
        **stripe_data
    )
    session.add(new_order)
    await session.commit()
    await session.refresh(new_order)
    stripe_utils.check_payment_status.apply_async(
      (new_order.id, new_order.stripe_session_id),
       countdown=180
      )
    return schemas.Order.from_orm(new_order)

async def get_order_by_id(order_id: int, session):
    try:
        result = await session.execute(select(models.Order).filter(models.Order.id == order_id))
        order = result.scalar_one()
        return order
    except NoResultFound:
        return None

async def list_orders(session):
    result = await session.execute(select(models.Order))
    orders = result.scalars().all()
    return list(orders)

async def update_order_payment_status(order_id: int, new_status: str, session):
    try:
        result = await session.execute(select(models.Order).filter(models.Order.id == order_id))
        order = result.scalar_one()
        order.payment_status = new_status
        await session.commit()
        await session.refresh(order)
        return order
    except NoResultFound:
        return None

async def delete_order(order_id: int, session):
    try:
        result = await session.execute(select(models.Order).filter(models.Order.id == order_id))
        order = result.scalar_one()
        await session.delete(order)
        await session.commit()
        return True
    except NoResultFound:
        return False

