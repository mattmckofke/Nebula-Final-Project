### 📊 4. Data Manipulation with Pandas

In this step, you will write Python scripts using Pandas to clean, transform, and aggregate the weather data you've stored in your PostgreSQL database. This prepares the data for effective visualization.

#### Step 4.1: Install Pandas

First, ensure that Pandas is installed in your Python environment. If not, install it using pip.

```bash
pip install pandas
```

#### Step 4.2: Fetch Data from PostgreSQL

Write a function to fetch data from your PostgreSQL database using Pandas. This function will utilize `pandas.read_sql_query` to convert SQL query results directly into a Pandas DataFrame.

```python
import pandas as pd
import psycopg2

def fetch_data_to_dataframe(connection):
    query = "SELECT * FROM weather_forecasts;"
    dataframe = pd.read_sql_query(query, connection)
    return dataframe

# Example usage with the db_connection from the previous steps
df = fetch_data_to_dataframe(db_connection)
print(df.head())
```

#### Step 4.3: Clean and Transform Data

Depending on the initial quality and format of your data, you may need to perform several cleaning and transformation steps. Common tasks include handling missing values, converting data types, and renaming columns for clarity.

```python
def clean_and_transform(dataframe):
    # Convert temperature to a numerical value
    dataframe['temperature'] = dataframe['temperature'].str.extract('(\d+)').astype(int)

    # Rename columns for clarity
    dataframe.rename(columns={'period': 'forecast_period', 'short_desc': 'description'}, inplace=True)

    # Fill any missing values, if necessary
    dataframe.fillna(method='ffill', inplace=True)

    return dataframe

# Clean and transform the DataFrame
df_cleaned = clean_and_transform(df)
print(df_cleaned.head())
```

#### Step 4.4: Aggregate Data

Perform any necessary aggregations to prepare the data for visualization. For example, you might want to summarize the data by period or calculate averages.

```python
def aggregate_data(dataframe):
    # Aggregate data by period, finding the average temperature
    aggregated_df = dataframe.groupby('forecast_period').agg({'temperature': 'mean'}).reset_index()
    aggregated_df['temperature'] = aggregated_df['temperature'].round(1)  # round the average temperature to one decimal
    return aggregated_df

# Aggregate the cleaned data
df_aggregated = aggregate_data(df_cleaned)
print(df_aggregated)
```

#### Step 4.5: Save the Processed Data (Optional)

If needed, save the cleaned and aggregated data back into your database or into a CSV file for offline analysis or further use.

```python
# To save to CSV
df_aggregated.to_csv('processed_weather_data.csv', index=False)

# To save back to the database (assuming a new table for processed data)
def save_processed_data(connection, dataframe):
    dataframe.to_sql('processed_weather_forecasts', con=connection, if_exists='replace', index=False)
    print("Processed data saved to the database successfully")

# Save processed data to the database
save_processed_data(db_connection, df_aggregated)
```

### 🚀 Next Steps

With your data now cleaned, transformed, and aggregated, you are ready to move on to creating visualizations with Matplotlib. This will be covered in the next step, where you will turn your structured data into insightful charts and graphs.

These detailed instructions ensure that you can effectively prepare your data for the analytical and visualization stages of your project, creating a solid foundation for meaningful insights.
