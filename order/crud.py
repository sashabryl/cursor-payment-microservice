from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from .models import Order
from .schemas import OrderCreate, OrderList
from database import get_db_session

async def create_order(order_data: OrderCreate):
    async with get_db_session() as session:
        new_order = Order(
            product_id=order_data.product_id,
            product_quantity=order_data.quantity,
            user_id=order_data.user_id,
            product_total=0  # Assuming calculation or external input is required here
        )
        session.add(new_order)
        await session.commit()
        await session.refresh(new_order)
        return new_order

async def get_order_by_id(order_id: int):
    async with get_db_session() as session:
        try:
            result = await session.execute(select(Order).filter(Order.id == order_id))
            order = result.scalar_one()
            return order
        except NoResultFound:
            return None

async def list_orders():
    async with get_db_session() as session:
        result = await session.execute(select(Order))
        orders = result.scalars().all()
        return orders

async def update_order_payment_status(order_id: int, new_status: str):
    async with get_db_session() as session:
        try:
            result = await session.execute(select(Order).filter(Order.id == order_id))
            order = result.scalar_one()
            order.payment_status = new_status
            await session.commit()
            return order
        except NoResultFound:
            return None

async def delete_order(order_id: int):
    async with get_db_session() as session:
        try:
            result = await session.execute(select(Order).filter(Order.id == order_id))
            order = result.scalar_one()
            await session.delete(order)
            await session.commit()
            return True
        except NoResultFound:
            return False
