from sqlalchemy import Column, Integer, String
from database import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    product_quantity = Column(Integer, nullable=False)
    product_total = Column(Integer, nullable=False)  # Changed from Float to Integer
    user_id = Column(Integer, nullable=False)
    stripe_session_id = Column(String, nullable=True)
    stripe_session_url = Column(String, nullable=True)

