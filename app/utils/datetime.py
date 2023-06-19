from datetime import date, timedelta


def is_valid_booking_date(booking_date: date) -> bool:
    return booking_date > date.today() + timedelta(days=1)


def get_date_from_year_month_day(year: int, month: int, day: int) -> date:
    return date(year, month, day)
