import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from psycopg2.extras import RealDictCursor
import io

# ================== Web Scraping ==================

def fetch_weather_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch web page. Status code: {response.status_code}")
    
def parse_weather_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Modify the selector based on the data you need
    forecast_items = soup.find_all('div', class_='tombstone-container')
    weather_data = []
    for item in forecast_items:
        period = item.find('p', class_='period-name').get_text()
        short_desc = item.find('p', class_='short-desc').get_text()
        temp = item.find('p', class_='temp').get_text()
        weather_data.append({'period': period, 'short_desc': short_desc, 'temp': temp})
    return weather_data

# ================== Database Connection ==================

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="weather-data",
            user="weather-data_owner",
            password="zAIomtVfW76G",
            host="ep-noisy-frost-a47foenm.us-east-1.aws.neon.tech"
        )
        connection.autocommit = True
        print("Connected to the database successfully")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        
def insert_weather_data(db_connection, weather_data):
    cursor = db_connection.cursor()
    query = """
    INSERT INTO weather_forecasts (period, short_desc, temperature)
    VALUES (%s, %s, %s);
    """
    for data in weather_data:
        cursor.execute(query, (data['period'], data['short_desc'], data['temp']))
    print("Data inserted successfully")
    
def fetch_data(db_connection):
    cursor = db_connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM weather_forecasts;")
    records = cursor.fetchall()
    for record in records:
        print(record)

# ================== Data Visualization ==================

def fetch_data_to_dataframe(connection):
    query = "SELECT * FROM weather_forecasts;"
    dataframe = pd.read_sql_query(query, connection)
    return dataframe

def clean_and_transform(dataframe):
    # Convert temperature to a numerical value
    dataframe['temperature'] = dataframe['temperature'].str.extract('(\d+)').astype(int)

    # Rename columns for clarity
    dataframe.rename(columns={'period': 'forecast_period', 'short_desc': 'description'}, inplace=True)

    # Fill any missing values, if necessary
    dataframe.fillna(method='ffill', inplace=True)

    return dataframe

def aggregate_data(dataframe):
    # Aggregate data by period, finding the average temperature
    aggregated_df = dataframe.groupby('forecast_period').agg({'temperature': 'mean'}).reset_index()
    aggregated_df['temperature'] = aggregated_df['temperature'].round(1)  # round the average temperature to one decimal
    return aggregated_df

def plot_temperature_trends(dataframe):
    plt.figure(figsize=(10, 5))  # Set the figure size
    plt.plot(dataframe['forecast_period'], dataframe['temperature'], marker='o')  # Plot a line chart
    plt.title('Temperature Trends Over Time')  # Add a title
    plt.xlabel('Forecast Period')  # Add an x-label
    plt.ylabel('Average Temperature (°F)')  # Add a y-label
    plt.grid(True)  # Add a grid
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Automatically adjust subplot parameters to give specified padding
    plt.show()
    
def plot_temperature_comparison(dataframe):
    plt.figure(figsize=(10, 5))
    plt.bar(dataframe['forecast_period'], dataframe['temperature'], color='blue')
    plt.title('Comparison of Average Temperatures')
    plt.xlabel('Forecast Period')
    plt.ylabel('Average Temperature (°F)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

url = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"

try:
    page_content = fetch_weather_page(url)
    weather_data = parse_weather_data(page_content)
    db_connection = connect_to_db()
except Exception as e:
    print(f"An error occurred: {e}")

# insert_weather_data(db_connection, weather_data)
# fetch_data(db_connection)

df = fetch_data_to_dataframe(db_connection)
df_cleaned = clean_and_transform(df)
df_aggregated = aggregate_data(df_cleaned)
print(df_aggregated)

# plot_temperature_trends(df)
# plot_temperature_comparison(df)






# ================== Data Persistence ==================

# To save to CSV
df_aggregated.to_csv('processed_weather_data.csv', index=False)

# To save back to the database (assuming a new table for processed data)
def save_processed_data(db_connection, dataframe):
    cursor = db_connection.cursor()
    query = """
    INSERT INTO processed_weather_forecasts (forecast_period, temperature)
    VALUES (%s, %s);
    """
    try:
        for _, row in dataframe.iterrows():
            cursor.execute(query, (row['forecast_period'], row['temperature']))
        db_connection.commit()
        print("Data inserted successfully")
    except Exception as e:
        db_connection.rollback()  # Rollback the transaction in case of an error
        print("Error inserting data:", e)
    finally:
        cursor.close()
        
def save_plot(dataframe):
    plt.figure()
    plt.plot(dataframe['forecast_period'], dataframe['temperature'], marker='o')
    plt.title('Temperature Trends Over Time')
    plt.xlabel('Forecast Period')
    plt.ylabel('Average Temperature (°F)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Save the figure
    plt.savefig('temperature_trends.png')  # You can specify different formats like PDF, SVG, etc.

# Save processed data to the database
# save_processed_data(db_connection, df_aggregated)

save_plot(df)