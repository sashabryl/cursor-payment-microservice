from pydantic import BaseModel
from order.models import PaymentStatus


class OrderCreate(BaseModel):
    product_id: int
    quantity: int
    user_id: int


class OrderList(BaseModel):
    id: int
    product_id: int
    quantity: int
    user_id: int
    created_at: str
    payment_status: PaymentStatus

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")
        }
