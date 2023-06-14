import requests
import argparse
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ws_api_key", help="API key for weatherstack service")
    parser.add_argument("--lat", help="lat for your area")
    parser.add_argument("--lon", help="lon for your area")
    return parser.parse_args()

def validate_api_key(api_key):
    if not api_key:
        raise ValueError("Please provide an API key either as an argument or in the .env file")

def get_weather(api_key, lat, lon):
    url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": f"{lat},{lon}"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data['current']

def calculate_density_altitude(pressure_hpa, temperature_c):
    pressure_altitude = 44330.8 * (1 - (pressure_hpa / 1013.25) ** 0.190263)
    density_altitude = pressure_altitude + (120 * (temperature_c - 15))
    return density_altitude

def convert_to_feet(density_altitude):
    return round(density_altitude * 3.28084)

def get_elevation(lat, lon):
    url = "https://api.open-elevation.com/api/v1/lookup"
    params = {"locations": f"{lat},{lon}"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    elevation_in_meters = data['results'][0]['elevation']
    elevation_in_ft = round(elevation_in_meters * 3.28084)
    return elevation_in_ft

def calculate_equivalent_altitude(actual_altitude_feet, density_altitude_feet):
    return int(actual_altitude_feet + density_altitude_feet)

def main():
    # Parse command line arguments
    args = parse_arguments()
    ws_api_key = args.ws_api_key or os.getenv('WS_API_KEY')
    lat = args.lat
    lon = args.lon

    # Validate API key
    validate_api_key(ws_api_key)

    # Get actual altitude
    actual_altitude_feet = get_elevation(lat, lon)

    # Get weather data
    weather_data = get_weather(ws_api_key, lat, lon)

    # Extract necessary data
    temperature_c = weather_data['temperature']
    pressure_hpa = weather_data['pressure']

    # Calculate density altitude
    density_altitude = calculate_density_altitude(pressure_hpa, temperature_c)
    density_altitude_feet = convert_to_feet(density_altitude)

    # Calculate equivalent altitude
    equivalent_altitude_feet = calculate_equivalent_altitude(actual_altitude_feet, density_altitude_feet)

    print(f"The equivalent altitude is {equivalent_altitude_feet} feet.")

if __name__ == "__main__":
    main()