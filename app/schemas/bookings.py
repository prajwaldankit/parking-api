from pydantic import BaseModel


class CreateBooking(BaseModel):
    customer_name: str
    license_plate: str
    year: int = 2023
    month: int = 11
    day: int = 23
