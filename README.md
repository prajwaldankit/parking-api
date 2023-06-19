# Car Park Booking API

This is a simple API for handling customers booking all-day parking at a single car park.

## Prerequisites

- Python 3.7 or higher
- Docker and Docker Compose

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/prajwaldankit/parking-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd parking-api
   ```

3. Build and run the Docker containers:

   ```bash
   docker-compose up -d --build
   ```

4. Access the API documentation at [http://localhost:8000/docs] .

## Usage

- Create a booking by sending a POST request to `/bookings`.
- Get all bookings for a specific date by sending a GET request to `/bookings/`.
- Get the total number of bookings for a specific date by sending a GET request to `/bookings/total/{booking_date}`.

## Database

- The API uses a PostgreSQL database for storing bookings and customer information. The database connection details can be configured in the `__init__.py` file in the `db` folder.
- The credentials are currently in the database folder. You can change it anytime from the `docker-compose.yml` file.

## Asumptions made

- The name and liscence plate of the customer is assumed to make a unique pair.

## Design decisions

- There are two tables with data for customers and bookings respectively, for future proofing. There are no queries for costumers currently but the impletentation can be made with a simple query.

## Trade-offs

- Due to time constraints, the bay number assigned to a booking could not be implemented. In future iterations, the `bays` table, which has already been initiated can be used to track even past users for that particular slot.
- We can also write test-cases in future iterations.

## Contributing

Contributions are welcome! If you find any issues or want to suggest improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

```


```
