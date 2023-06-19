import asyncpg

pool = None


async def connect_to_database():
    global pool
    pool = await asyncpg.create_pool(
        user="root",
        password="password",
        database="parking_db",
        host="db"
    )
    async with pool.acquire() as connection:
        await connection.execute(
            """
            CREATE TABLE IF NOT EXISTS customers (
                id SERIAL PRIMARY KEY,
                name TEXT,
                license_plate TEXT
            )
            """
        )
        await connection.execute(
            """
            CREATE TABLE IF NOT EXISTS bookings (
                id SERIAL PRIMARY KEY,
                customer_id INT,
                booking_date DATE,
                created_at TIMESTAMPTZ,
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            )
            """
        )
        return pool


async def close_database_connection():
    await pool.close()
