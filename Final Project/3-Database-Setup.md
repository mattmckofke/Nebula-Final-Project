### 🗃️ 3. Database Setup

In this step, we will establish a PostgreSQL database on Neon.tech, design the database schema, and configure connections securely.

#### Step 3.1: Sign Up and Create a PostgreSQL Database on Neon

First, you need to create an account on Neon and set up a PostgreSQL database.

1. **Go to [Neon.tech](https://www.neon.tech/) and sign up for an account.**
2. **Follow the instructions to create a new PostgreSQL database.**
3. **Once created, note down the credentials provided (host, database name, user, and password) as you will need them to connect to your database.**

#### Step 3.2: Design the Database Schema

Plan and create the tables you need for storing weather data. For this example, let's create a simple table to store the weather forecasts.

```sql
-- Connect to your PostgreSQL database using a client like pgAdmin or via command line

CREATE TABLE weather_forecasts (
    id SERIAL PRIMARY KEY,
    period VARCHAR(50),
    short_desc VARCHAR(255),
    temperature VARCHAR(50),
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Step 3.3: Install psycopg2

Install the `psycopg2` library in Python to enable interaction with PostgreSQL.

```bash
pip install psycopg2-binary
```

#### Step 3.4: Connect to the Database from Python

Write a Python script to establish a connection to your PostgreSQL database using the credentials from Step 3.1.

```python
import psycopg2
from psycopg2.extras import RealDictCursor

def connect_to_db():
    try:
        # Replace 'dbname', 'user', 'password', and 'host' with your database details
        connection = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_database_host"
        )
        connection.autocommit = True
        print("Connected to the database successfully")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")

# Example usage
db_connection = connect_to_db()
```

#### Step 3.5: Write Data to the Database

Create a function to insert weather data into the database.

```python
def insert_weather_data(db_connection, weather_data):
    cursor = db_connection.cursor()
    query = """
    INSERT INTO weather_forecasts (period, short_desc, temperature)
    VALUES (%s, %s, %s);
    """
    for data in weather_data:
        cursor.execute(query, (data['period'], data['short_desc'], data['temp']))
    print("Data inserted successfully")

# Assuming 'weather_data' is the data scraped and parsed previously
# insert_weather_data(db_connection, weather_data)
```

#### Step 3.6: Test the Database Operations

Ensure that you can successfully write and retrieve data from your database.

```python
def fetch_data(db_connection):
    cursor = db_connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM weather_forecasts;")
    records = cursor.fetchall()
    for record in records:
        print(record)

# Fetch and display data to test the setup
fetch_data(db_connection)
```

### 🚀 Next Steps

Now that your database is set up and you are able to store scraped data, you can proceed to the next part of your project, which involves data manipulation using Pandas. This step will be crucial for preparing your data for visualization.

By following these detailed instructions, you will have a robust database setup ready to handle and store data for your application.
