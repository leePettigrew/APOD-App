import json
import os
import csv
from datetime import datetime


def format_date(date_str):
    """
    Formats a date string from YYYY-MM-DD to DD/MM/YYYY.

    Parameters:
    - date_str (str): The date string in YYYY-MM-DD format.

    Returns:
    - str: The date string in DD/MM/YYYY format.
    """
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except ValueError:
        return date_str  # Return as-is if the format doesn't match

#Changing the dates again because i dont like the format
def read_apod_data():
    """
    Reads the 'apod_data.json' file and loads its content into a Python dictionary.

    Returns:
    - data_list (list): List of dictionaries containing APOD data.
    """
    try:
        with open('apod_data.json', 'r', encoding='utf-8') as f:
            data_list = json.load(f)
        # Check if the file is empty
        if not data_list:
            print("Error: 'apod_data.json' is empty.")
            return None
        else:
            print(f"Successfully loaded data from 'apod_data.json'.\n")
            # Loop through the data and print date and title
            for entry in data_list:
                print(f"Date: {format_date(entry.get('date'))}, Title: {entry.get('title')}")
            return data_list
    except FileNotFoundError:
        print("Error: 'apod_data.json' file not found.")
        return None
    except PermissionError:
        print("Error: Permission denied when accessing 'apod_data.json'.")
        return None
    except json.JSONDecodeError:
        print("Error: 'apod_data.json' is empty or corrupt.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def analyze_apod_media():
    """
    Analyzes the APOD data to count the total number of images and videos,
    and identifies the date with the most detailed explanation.
    """
    try:
        with open('apod_data.json', 'r', encoding='utf-8') as f:
            data_list = json.load(f)
        if not data_list:
            print("Error: 'apod_data.json' is empty.")
            return
    except FileNotFoundError:
        print("Error: 'apod_data.json' file not found.")
        return
    except PermissionError:
        print("Error: Permission denied when accessing 'apod_data.json'.")
        return
    except json.JSONDecodeError:
        print("Error: 'apod_data.json' is empty or corrupt.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    total_images = 0
    total_videos = 0
    longest_explanation = ''
    longest_explanation_date = ''

    for entry in data_list:
        media_type = entry.get('media_type')
        if media_type == 'image':
            total_images += 1
        elif media_type == 'video':
            total_videos += 1
        # Check for the longest explanation
        explanation = entry.get('explanation', '')
        if len(explanation) > len(longest_explanation):
            longest_explanation = explanation
            longest_explanation_date = entry.get('date')

    print("\nAnalysis Results:")
    print(f"Total number of images: {total_images}")
    print(f"Total number of videos: {total_videos}")
    print(f"The date with the most detailed explanation is {format_date(longest_explanation_date)}")


def write_apod_summary_to_csv():
    """
    Extracts date, title, media type, and URL from 'apod_data.json' and writes to 'apod_summary.csv'.
    If the CSV file exists, new entries are appended. If the file does not exist, a new one is created.
    """
    try:
        with open('apod_data.json', 'r', encoding='utf-8') as f:
            data_list = json.load(f)
        if not data_list:
            print("Error: 'apod_data.json' is empty.")
            return
    except FileNotFoundError:
        print("Error: 'apod_data.json' file not found.")
        return
    except PermissionError:
        print("Error: Permission denied when accessing 'apod_data.json'.")
        return
    except json.JSONDecodeError:
        print("Error: 'apod_data.json' is empty or corrupt.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Define CSV file name
    csv_file = 'apod_summary.csv'
    file_exists = os.path.isfile(csv_file)
    try:
        # Read existing dates to avoid duplicates
        existing_dates = set()
        if file_exists:
            with open(csv_file, 'r', encoding='utf-8') as readfile:
                reader = csv.DictReader(readfile)
                for row in reader:
                    existing_dates.add(row['date'])
            print(f"Loaded existing dates from '{csv_file}'.")
        else:
            print(f"'{csv_file}' not found. Creating a new one.")

        with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['date', 'title', 'media_type', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # If file does not exist, write header, else append new entries
            if not file_exists:
                writer.writeheader()
                print(f"Header written to '{csv_file}'.")
            # Write entries
            new_entries = 0
            for entry in data_list:
                date = format_date(entry.get('date'))
                if date in existing_dates:
                    continue  # Skip if date already exists
                writer.writerow({
                    'date': date,
                    'title': entry.get('title'),
                    'media_type': entry.get('media_type'),
                    'url': entry.get('url')
                })
                new_entries += 1
            if new_entries > 0:
                print(f"Successfully appended {new_entries} new entries to '{csv_file}'.")
            else:
                print(f"No new entries were added to '{csv_file}'.")
    except PermissionError:
        print(f"Error: Permission denied when writing to '{csv_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred while writing to CSV: {e}")


if __name__ == "__main__":
    # Read and load the data
    print("Reading APOD data...")
    data = read_apod_data()

    # Analyze the data
    if data:
        print("\nAnalyzing APOD data...")
        analyze_apod_media()

        # Write summary to CSV
        print("\nWriting summary to CSV...")
        write_apod_summary_to_csv()
    else:
        print("Data could not be loaded. Exiting program.")
