from pydantic import BaseModel


class RateBase(BaseModel):
    pass


class Price(BaseModel):
    total_price: float
