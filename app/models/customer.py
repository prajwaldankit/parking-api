from . import BaseModel


class Customer(BaseModel):
    id: int
    name: str
    license_plate: str


async def create_customer(pool, customer: Customer) -> int:
    async with pool.acquire() as connection:
        query = "INSERT INTO customers (name, license_plate) VALUES ($1, $2) RETURNING id"
        return await connection.fetchval(query, customer.name, customer.license_plate)


async def get_customer_by_id(pool, customer_id: int):
    async with pool.acquire() as connection:
        query = "SELECT * FROM customers WHERE id = $1"
        result = await connection.fetchrow(query, customer_id)
        if result:
            return Customer(**result)
        else:
            return None


async def get_customer_by_name_and_liscence_plate(pool, name: str, licence_plate: str):
    async with pool.acquire() as connection:
        customer_query = "SELECT * FROM customers WHERE name = $1 AND license_plate = $2"
        result = await connection.fetchrow(
            customer_query,
            name,
            licence_plate
        )
        if result:
            return Customer(**result)
        else:
            return None


async def get_or_create_customer(pool, name: str, license_plate: str) -> int:
    async with pool.acquire() as connection:
        query = "SELECT * FROM customers WHERE name = $1 AND license_plate = $2"
        result = await connection.fetchrow(query, name, license_plate)
        if result:
            return Customer(**result).id
        else:
            query = "INSERT INTO customers (name, license_plate) VALUES ($1, $2) RETURNING id"
            customer_id = await connection.fetchval(query, name, license_plate)
            return Customer(id=customer_id, name=name, license_plate=license_plate).id
