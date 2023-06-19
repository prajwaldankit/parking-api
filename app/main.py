from schemas.bookings import CreateBooking
from datetime import date
from fastapi import FastAPI, HTTPException
from utils.datetime import is_valid_booking_date

from db import connect_to_database, close_database_connection
from models.booking import create_booking, get_bookings_by_date, check_existing_booking, get_total_bookings_by_date
from models.customer import get_or_create_customer

app = FastAPI()

pool = None


@app.on_event("startup")
async def startup():
    global pool
    pool = await connect_to_database()


@app.on_event("shutdown")
async def shutdown():
    await close_database_connection()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Parking API!"}


@app.post("/bookings")
async def create_booking_handler(booking_details: CreateBooking):
    year = booking_details.year
    month = booking_details.month
    day = booking_details.day
    booking_date = date(year, month, day)
    if not is_valid_booking_date(booking_date):
        raise HTTPException(
            status_code=400, detail="Booking date must be at least 24 hours in advance!")
    customer_id = await get_or_create_customer(pool, booking_details.customer_name, booking_details.license_plate)

    existing_booking = await check_existing_booking(pool, customer_id, booking_date=booking_date)
    if existing_booking:
        raise HTTPException(
            status_code=400, detail="Customer has already made a booking for the given date!")
    number_of_bookings = await get_total_bookings_by_date(pool, booking_date)
    if number_of_bookings >= 4:
        raise HTTPException(
            status_code=400, detail="No bays are available for that date!")

    booking_id = await create_booking(pool, customer_id, booking_date)

    return {"message": "Booking successful!", "booking_id": booking_id}


@app.get("/bookings/")
async def get_bookings(year: int = 2023, month: int = 11, day: int = 23):
    booking_date = date(year, month, day)
    return await get_bookings_by_date(pool, booking_date)
