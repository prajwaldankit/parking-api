# from db import pool
from . import BaseModel


from datetime import date, datetime
from typing import List


class Booking(BaseModel):
    id: int
    customer_id: int
    booking_date: date
    created_at: datetime = datetime.now()


async def create_booking(pool, customer_id, booking_date) -> int:
    query = "INSERT INTO bookings (customer_id, booking_date, created_at) VALUES ($1, $2, $3) RETURNING id"
    async with pool.acquire() as connection:
        return await connection.fetchval(query, customer_id, booking_date, datetime.now())


async def get_bookings_by_date(pool, booking_date: date) -> List[Booking]:
    query = "SELECT * FROM bookings WHERE DATE(booking_date) = $1"
    async with pool.acquire() as connection:
        results = await connection.fetch(query, booking_date)
        return [Booking(**result) for result in results]


async def check_existing_booking(pool, customer_id, booking_date) -> bool:
    booking_query = "SELECT * FROM bookings WHERE customer_id = $1 AND booking_date::date = $2"
    async with pool.acquire() as connection:
        existing_booking = await connection.fetchrow(
            booking_query,
            customer_id,
            booking_date
        )
        return True if existing_booking else False


async def get_total_bookings_by_date(pool, booking_date: date) -> int:
    query = "SELECT COUNT(*) AS total_bookings FROM bookings WHERE DATE(booking_date) = $1"
    async with pool.acquire() as connection:
        result = await connection.fetchval(query, booking_date)
        return result
