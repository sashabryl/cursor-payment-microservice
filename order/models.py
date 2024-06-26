import datetime

from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from sqlalchemy import Enum
import enum

class PaymentStatus(enum.Enum):
    UNPAID = "UNPAID"
    PAID = "PAID"

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    product_quantity = Column(Integer, nullable=False)
    product_total = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    stripe_session_id = Column(String, nullable=True)
    stripe_session_url = Column(String, nullable=True)
    payment_status = Column(Enum(PaymentStatus), default=PaymentStatus.UNPAID, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
