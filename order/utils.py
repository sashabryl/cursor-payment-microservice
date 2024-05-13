import stripe
from order.schemas import OrderCreate
from fastapi import HTTPException
from settings import settings
from order.models import Order, PaymentStatus
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal

stripe.api_key = settings.stripe_secret_key

async def create_checkout_session(order_data: OrderCreate) -> dict:
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'Product ID {order_data.product_id}',
                    },
                    'unit_amount': order_data.product_total * 100 // order_data.product_quantity,
                },
                'quantity': order_data.product_quantity,
            }],
            mode='payment',
            success_url='https://google.com',
            cancel_url='https://youtube.com',
        )
        return {
            'stripe_session_url': checkout_session.url,
            'stripe_session_id': checkout_session.id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
