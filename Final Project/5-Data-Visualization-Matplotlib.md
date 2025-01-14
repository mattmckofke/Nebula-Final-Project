### 📉 5. Data Visualization with Matplotlib

Matplotlib is a powerful plotting library in Python that enables you to produce figures and charts in a wide variety of formats. We'll use it to create visualizations from the cleaned and aggregated data you prepared in the previous steps.

#### Step 5.1: Install Matplotlib

Ensure Matplotlib is installed in your Python environment. If not, install it using pip.

```bash
pip install matplotlib
```

#### Step 5.2: Import Matplotlib

Begin by importing Matplotlib in your Python script where you'll be creating the visualizations.

```python
import matplotlib.pyplot as plt
```

#### Step 5.3: Load Your Data

For the purpose of this example, assume you have your data in a Pandas DataFrame from the previous step. If not, you can read it from a CSV or directly from the database.

```python
import pandas as pd

# If reading from a CSV file
df = pd.read_csv('processed_weather_data.csv')

# Or, if loading directly from the database, you can use the previous function to load data to DataFrame
```

#### Step 5.4: Create a Line Plot

Let's create a simple line plot showing the temperature trends over different forecast periods.

```python
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

# Call the function with the aggregated DataFrame
plot_temperature_trends(df)
```

#### Step 5.5: Create a Bar Chart

Next, we can create a bar chart to compare average temperatures across different periods.

```python
def plot_temperature_comparison(dataframe):
    plt.figure(figsize=(10, 5))
    plt.bar(dataframe['forecast_period'], dataframe['temperature'], color='blue')
    plt.title('Comparison of Average Temperatures')
    plt.xlabel('Forecast Period')
    plt.ylabel('Average Temperature (°F)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Call the function with the DataFrame
plot_temperature_comparison(df)
```

#### Step 5.6: Save Plots to Files (Optional)

If you need to save these plots for reports or presentations, you can easily do so in various formats such as PNG, PDF, etc.

```python
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

# Call the save function
save_plot(df)
```

### 🚀 Next Steps

With your visualizations now created, the next step is to integrate these charts into your Flask API so they can be served dynamically in response to user requests. This will allow users to access updated visualizations based on the latest data.

These detailed steps equip you to effectively use Matplotlib to visualize data, enhancing the interpretability of your analysis and making your findings accessible and impactful.
