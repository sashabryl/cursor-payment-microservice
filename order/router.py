from fastapi import APIRouter, HTTPException, status, Depends
from order import models
from order.schemas import OrderCreate, Order
from order.crud import create_order, get_order_by_id, list_orders, update_order_payment_status, delete_order
from typing import List
from database import get_db_session

router = APIRouter()

@router.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order_endpoint(order_data: OrderCreate, db_session=Depends(get_db_session)):
    order = await create_order(order_data, db_session)
    if not order:
        raise HTTPException(status_code=400, detail="Error creating order")
    return order

@router.get("/orders/", response_model=list[Order])
async def list_orders_endpoint(db_session=Depends(get_db_session)):
    orders = await list_orders(db_session)
    return orders

@router.put("/orders/{order_id}", response_model=Order)
async def update_order_status_endpoint(order_id: int, new_status: models.PaymentStatus, db_session=Depends(get_db_session)):
    order = await update_order_payment_status(order_id, new_status, db_session)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order_endpoint(order_id: int, db_session=Depends(get_db_session)):
    success = await delete_order(order_id, db_session)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"detail": "Order deleted successfully"}
