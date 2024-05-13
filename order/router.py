from fastapi import APIRouter, HTTPException, status, Depends
from order import models
from order.schemas import OrderCreate, Order
from order.crud import create_order, list_orders, update_order_payment_status, delete_order
from database import get_db_session
from settings import settings

router = APIRouter()

def check_api_key(api_key: str):
    if api_key != settings.secret_key:
        raise HTTPException(status_code=401, detail="Unauthorized")

@router.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order_endpoint(api_key: str, order_data: OrderCreate, 
                                db_session=Depends(get_db_session)):
    check_api_key(api_key)
    order = await create_order(order_data, db_session)
    if not order:
        raise HTTPException(status_code=400, detail="Error creating order")
    return order

@router.get("/orders/", response_model=list[Order])
async def list_orders_endpoint(api_key: str, db_session=Depends(get_db_session)):
    check_api_key(api_key)
    orders = await list_orders(db_session)
    return orders

@router.put("/orders/{order_id}", response_model=Order)
async def update_order_status_endpoint(api_key: str, order_id: int, 
                                       new_status: models.PaymentStatus, 
                                       db_session=Depends(get_db_session)):
    check_api_key(api_key)
    order = await update_order_payment_status(order_id, new_status, db_session)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order_endpoint(api_key: str, order_id: int, 
                                db_session=Depends(get_db_session)):
    check_api_key(api_key)
    success = await delete_order(order_id, db_session)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"detail": "Order deleted successfully"}
