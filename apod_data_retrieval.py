# apod_data_retrieval.py

# Import necessary libraries
import os
from dotenv import load_dotenv  # To load environment variables from .env file
import requests
import datetime
import time
import json

# Load the .env file to access environment variables
load_dotenv()

def get_apod_data(api_key, date):
    """
    Fetches Astronomy Picture of the Day (APOD) data for a specific date from NASA's APOD API.

    Parameters:
    - api_key (str): Your NASA API key.
    - date (str): The date for which to fetch the APOD data in 'DD/MM/YYYY' format.

    Returns:
    - dict: A dictionary containing the APOD data for the specified date.
    """
    try:
        # Convert date from DD/MM/YYYY to YYYY-MM-DD for the API
        date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
        api_date = date_obj.strftime('%Y-%m-%d')

        # API endpoint for NASA's APOD
        url = 'https://api.nasa.gov/planetary/apod'

        # Parameters for the API request
        params = {
            'api_key': api_key,
            'date': api_date,
        }

        # Send GET request to the API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract the required fields
        result = {
            'date': data.get('date'),
            'title': data.get('title'),
            'url': data.get('url'),
            'explanation': data.get('explanation'),
            'media_type': data.get('media_type')
        }

        return result

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for date {date}: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred for date {date}: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred for date {date}: {timeout_err}")
    except Exception as err:
        print(f"An unexpected error occurred for date {date}: {err}")

def fetch_multiple_apod_data(api_key, start_date, end_date):
    """
    Fetches APOD data for a range of dates and saves it to 'apod_data.json'.

    Parameters:
    - api_key (str): Your NASA API key.
    - start_date (str): The start date in 'DD/MM/YYYY' format.
    - end_date (str): The end date in 'DD/MM/YYYY' format.
    """
    # Convert string dates from DD/MM/YYYY to datetime objects
    #Could have read the documentation wrong but i don't like the format of the dates
    try:
        start_dt = datetime.datetime.strptime(start_date, '%d/%m/%Y')
        end_dt = datetime.datetime.strptime(end_date, '%d/%m/%Y')
    except ValueError as ve:
        print(f"Date format error: {ve}")
        return

    # Calculate the number of days between start and end dates
    delta = datetime.timedelta(days=1)
    current_date = start_dt

    # Initialize a list to hold all the APOD data
    data_list = []

    # Check if 'apod_data.json' already exists
    if os.path.exists('apod_data.json'):
        # Load existing data to avoid duplicates
        try:
            with open('apod_data.json', 'r') as f:
                data_list = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # If the file is empty or not found, start with an empty list
            data_list = []
    else:
        data_list = []

    # Keep track of dates we already have data for
    existing_dates = set(item['date'] for item in data_list)

    # Loop through each date in the range
    while current_date <= end_dt:
        # Format the date as DD/MM/YYYY for display and input to get_apod_data
        date_str = current_date.strftime('%d/%m/%Y')

        # Convert date to YYYY-MM-DD to check against existing data
        api_date_str = current_date.strftime('%Y-%m-%d')

        if api_date_str in existing_dates:
            print(f"Data for {date_str} already exists. Skipping to next date.")
        else:
            # Fetch data for the current date
            data = get_apod_data(api_key, date_str)
            if data:
                data_list.append(data)
                # Save the updated data list to the JSON file
                print(f"Data added for {date_str}")
                try:
                    with open('apod_data.json', 'w') as f:
                        json.dump(data_list, f, indent=4)
                except IOError as e:
                    print(f"Error writing to file: {e}")
        # Respect the API rate limit (barely)
        time.sleep(0.1)
        # Move to the next date
        current_date += delta

if __name__ == "__main__":
    # Retrieve the API key from environment variables
    api_key = os.getenv('API_KEY')

    if not api_key:
        print("Error: Please set the API_KEY environment variable.")
    else:
        # Define the date range for data retrieval in DD/MM/YYYY format
        start_date = '01/01/2020'
        end_date = '31/12/2020'
        # This should be plenty of data
        print(f"Fetching APOD data from {start_date} to {end_date}...")
        fetch_multiple_apod_data(api_key, start_date, end_date)
        print("Data retrieval complete!")
