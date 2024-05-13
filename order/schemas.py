import datetime

from pydantic import BaseModel, field_validator
from order.models import PaymentStatus


class OrderCreate(BaseModel):
    product_id: int
    product_quantity: int
    product_total: int
    user_id: int


class Order(BaseModel):
    id: int
    product_id: int
    product_quantity: int
    product_total: int
    user_id: int
    created_at: datetime.datetime
    payment_status: PaymentStatus
    stripe_session_id: str
    stripe_session_url: str

    class Config:
        from_attributes = True
    
    @field_validator("created_at")
    @classmethod
    def validate_created_at(cls, v: datetime.datetime):
        return v.strftime("%Y/%m/%d, %H:%M")
