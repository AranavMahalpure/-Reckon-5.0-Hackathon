from flask import Flask, render_template, request
import requests
from geopy.geocoders import Nominatim

# Create a Flask application instance
app = Flask(__name__)

from geopy.geocoders import Nominatim

# Create a geolocator instance
geolocator = Nominatim(user_agent="weather_app")

# Function to fetch weather data from API
def fetch_weather_data(location_name):
    # Get latitude and longitude based on location name
    location = geolocator.geocode(location_name)
    if location:
        lat = location.latitude
        lon = location.longitude
        
        # API URL with latitude and longitude
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=877bf7d6e49041739cd8d0799d83a8f4'
        
        # Send a GET request to the API endpoint
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Process the data as needed
            relevant_data = {
                "temp_max": [(item['main']['temp_max'] - 273.15) for item in data['list']],  # Kelvin to Celsius
                "windspeed": [(item['wind']['speed'] * 3.6) for item in data['list']],  # m/s to km/h
                "pressure": [item['main']['pressure'] for item in data['list']],
                "feelslike": [(item['main']['feels_like'] - 273.15) for item in data['list']],  # Kelvin to Celsius
                "visibility": [(item['visibility']/1000) for item in data['list']],  # meters to kilometers
                "humidity": [(item['main']['humidity'] / 100) for item in data['list']],
                "temp_min": [(item['main']['temp_min'] - 273.15) for item in data['list']],  # percentage to fraction
            }
            return relevant_data
        else:
            # Return None if request failed
            print("Error fetching data from OpenWeatherMap API:", response.status_code)
            return None
    else:
        print("Location not found.")
        return None


# Define a route for the index page
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Define a route for form submission
@app.route('/weather', methods=['POST'])
def weather():
    # Get the location from the form data
    location = request.form.get("location")
    # Fetch weather data for the provided location
    weather_data = fetch_weather_data(location)
    # Render the weather.html template with weather data
    return render_template('weather.html', weather_data=weather_data)
# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
