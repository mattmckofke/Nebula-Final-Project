from flask import Flask, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

# Ensure that Matplotlib uses a non-interactive backend to generate plots
plt.switch_backend('Agg')

@app.route('/temperature_trends')
def temperature_trends():
    # Generate the plot
    fig, ax = plt.subplots()
    ax.plot(['Monday', 'Tuesday', 'Wednesday'], [22, 25, 28], marker='o')
    ax.set(title='Weekly Temperature Trends', xlabel='Day of the Week', ylabel='Temperature (°C)')
    ax.grid(True)

    # Save it to a bytes buffer instead of a file
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    # Send the buffer as a response
    return send_file(buf, mimetype='image/png')

@app.route('/temperature_comparison')
def temperature_comparison():
    # Generate the bar chart
    fig, ax = plt.subplots()
    ax.bar(['Monday', 'Tuesday', 'Wednesday'], [22, 25, 28], color='blue')
    ax.set(title='Comparison of Temperatures', xlabel='Day of the Week', ylabel='Temperature (°C)')

    # Save it to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    # Send the buffer as a response
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
