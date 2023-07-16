from decimal import Decimal
from datetime import date

from fastapi import APIRouter, HTTPException, status

from app.services.database.schemas.rates import Price
from app.services.database.models.rates import Rates

router = APIRouter()


@router.get('/rates', response_model=Price)
async def user_registration(
    date: date,
    cargo_type: str,
    price: float,
):
    rate = await Rates.get(date=date, cargo_type=cargo_type.capitalize())
    return Price(total_price=rate.rate * Decimal(price))
