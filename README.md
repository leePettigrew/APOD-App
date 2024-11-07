# Data Analysis Project

**Author:** Lee Pettigrew  
**Student Number:** x20730039

---

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Setting Up the NASA API Key](#setting-up-the-nasa-api-key)
4. [Project Components](#project-components)
   - [1. APOD Data Retrieval (`apod_data_retrieval.py`)](#1-apod-data-retrieval-apod_data_retrievalpy)
   - [2. APOD Data Processing (`apod_data_processing.py`)](#2-apod-data-processing-apod_data_processingpy)
   - [3. NumPy Array Manipulation (`numpy_array_thing.py`)](#3-numpy-array-manipulation-numpy_array_thingpy)
   - [4. Iris Data Analysis (`iris_data_analysis_thing.py`)](#4-iris-data-analysis-iris_data_analysis_thingpy)
5. [Resetting the Project](#resetting-the-project)
6. [Usage Guide](#usage-guide)
   - [Running the Scripts](#running-the-scripts)
   - [Expected Outputs](#expected-outputs)
7. [Troubleshooting](#troubleshooting)
8. [Conclusion](#conclusion)
9. [Acknowledgments](#acknowledgments)

---

## Introduction

Welcome to the **Data Analysis Project**! This project encompasses a series of Python scripts designed to perform data retrieval, processing, and analysis tasks across different datasets. The primary focus areas include:

- **NASA's Astronomy Picture of the Day (APOD) API**
- **NumPy Array Manipulation and Statistical Analysis**
- **Pandas DataFrame Operations on the Iris Dataset**

This comprehensive README aims to guide you through each component of the project, providing detailed explanations, setup instructions, and usage guidelines.

---

## Project Structure

The project directory contains the following files:

- **Python Scripts:**
  - `apod_data_retrieval.py`
  - `apod_data_processing.py`
  - `numpy_array_thing.py`
  - `iris_data_analysis_thing.py`
- **Data Files:**
  - `iris.csv` (Ensure you download and place it in the project directory)
- **Output Files:**
  - `apod_data.json`
  - `apod_summary.csv`
  - `iris_corrected.csv`
  - `iris_scatter_with_regression.pdf`
  - `iris_pair_plot.png`
- **Configuration Files:**
  - `.env` (to store your NASA API key)
  - `requirements.txt` (List of required Python packages)
- **Documentation:**
  - `README.md` (This detailed documentation)

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.6 or higher**
- **pip** (Python package installer)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/leePettigrew/APOD-App.git
   cd APOD-App-master
   ```

2. **Set Up a Virtual Environment (Recommended)**

   Create and activate a virtual environment to manage project dependencies:

   - **Windows:**

     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Required Packages**

   Install the necessary Python libraries using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Iris Dataset**

   Ensure the `iris.csv` file is placed in the project directory. If not already present, download it from Moodle or the provided source.

### Setting Up the NASA API Key

To access NASA's APOD API, you'll need to provide your own API key. Follow these steps:

1. **Obtain a NASA API Key**

   - Visit [NASA's API Portal](https://api.nasa.gov/) and sign up for an API key.
   - You will receive an API key, usually a string of letters and numbers.

2. **Create a `.env` File**

   - In the project directory, create a new file named `.env`.
   - Open the `.env` file in a text editor and add the following line:

     ```plaintext
     API_KEY=YOUR_NASA_API_KEY_HERE
     ```

     Replace `YOUR_NASA_API_KEY_HERE` with the API key you obtained from NASA.

3. **Ensure `python-dotenv` is Installed**

   The `python-dotenv` package is included in `requirements.txt`. It allows the scripts to read environment variables from the `.env` file.

   If you haven't already installed the packages, run:

   ```bash
   pip install -r requirements.txt
   ```

4. **Verify the Setup**

   - Your `.env` file should be in the same directory as `apod_data_retrieval.py`.
   - Do **not** commit the `.env` file to any public repositories, as it contains sensitive information.

---

## Project Components

### 1. APOD Data Retrieval (`apod_data_retrieval.py`)

**Description:**

This script interacts with NASA's Astronomy Picture of the Day (APOD) API to retrieve data for a specified date range. It collects information such as the image URL, title, explanation, and media type for each date.

**Key Features:**

- Fetches data for multiple dates.
- Handles API rate limits by including delays between requests.
- Saves the retrieved data into `apod_data.json`.

**Usage Instructions:**

- Ensure your NASA API key is set up in the `.env` file as described above.
- Run the script:

  ```bash
  python apod_data_retrieval.py
  ```

- The script will read your API key from the `.env` file and retrieve the APOD data.

### 2. APOD Data Processing (`apod_data_processing.py`)

**Description:**

Processes the data collected by `apod_data_retrieval.py`. It performs analysis on the APOD dataset and generates a summary CSV file.

**Key Features:**

- Reads `apod_data.json` and handles exceptions if the file is missing or corrupted.
- Counts the number of images and videos.
- Identifies the entry with the longest explanation.
- Writes a summary to `apod_summary.csv`, including date, title, media type, and URL.

**Usage Instructions:**

- Ensure `apod_data.json` is present in the project directory.
- Run the script:

  ```bash
  python apod_data_processing.py
  ```

### 3. NumPy Array Manipulation (`numpy_array_thing.py`)

**Description:**

Creates and manipulates a 2D NumPy array with specific conditions and performs statistical analyses.

**Key Features:**

- Generates a 20x5 array of random integers between 10 and 100.
- Ensures the sum of each row is even and the total sum is a multiple of 5.
- Extracts elements divisible by both 3 and 5.
- Replaces elements greater than 75 with the mean of the array.
- Calculates mean, standard deviation, median, and variance.

**Usage Instructions:**

- Run the script:

  ```bash
  python numpy_array_thing.py
  ```

- Observe the console output for results.

### 4. Iris Data Analysis (`iris_data_analysis_thing.py`)

**Description:**

Performs comprehensive data analysis on the Iris dataset, including data cleaning, feature engineering, correlation analysis, and visualization.

**Key Features:**

- Loads `iris.csv` and displays dataset information.
- Corrects known errors in specific rows.
- Adds new features: Petal Ratio and Sepal Ratio.
- Calculates pairwise correlations and identifies significant relationships.
- Creates a scatter plot with regression lines and a pair plot for visualization.
- Saves outputs to `iris_corrected.csv`, `iris_scatter_with_regression.pdf`, and `iris_pair_plot.png`.

**Usage Instructions:**

- Ensure `iris.csv` is in the project directory.
- Run the script:

  ```bash
  python iris_data_analysis_thing.py
  ```

---

## Resetting the Project

To start fresh and delete generated data:

1. **Delete Output Files:**

   - `apod_data.json`
   - `apod_summary.csv`
   - `iris_corrected.csv`
   - `iris_scatter_with_regression.pdf`
   - `iris_pair_plot.png`

2. **Re-run the Scripts:**

   Follow the usage instructions for each script to regenerate the data and outputs.

---

## Usage Guide

### Running the Scripts

Execute each script individually as needed:

```bash
python apod_data_retrieval.py       # Retrieves APOD data from NASA's API
python apod_data_processing.py      # Processes APOD data and creates a summary
python numpy_array_thing.py         # Performs NumPy array manipulation and analysis
python iris_data_analysis_thing.py  # Analyzes the Iris dataset and generates visualizations
```

### Expected Outputs

- **`apod_data_retrieval.py`**:

  - Generates `apod_data.json` containing APOD data for the specified date range.

- **`apod_data_processing.py`**:

  - Produces `apod_summary.csv` summarizing the APOD data.

- **`numpy_array_thing.py`**:

  - Outputs results to the console, including the adjusted array and statistical calculations.

- **`iris_data_analysis_thing.py`**:

  - Saves:
    - `iris_corrected.csv`: The cleaned and enhanced dataset.
    - `iris_scatter_with_regression.pdf`: Scatter plot with regression lines.
    - `iris_pair_plot.png`: Comprehensive pair plot.

---

## Troubleshooting

- **API Key Errors (APOD Scripts):**

  - Ensure your NASA API key is correctly set in the `.env` file.
  - Check for typos in the `.env` file (e.g., extra spaces or incorrect variable names).
  - Do not enclose the API key in quotes.

- **File Not Found Errors:**

  - Verify that all necessary files (`iris.csv`, `apod_data.json`, etc.) are in the project directory.
  - Ensure filenames match exactly, including case sensitivity.

- **Module Not Found Errors:**

  - Confirm that all required packages are installed using `requirements.txt`.
  - Activate your virtual environment before running the scripts.

- **Permission Denied Errors:**

  - Check file and directory permissions.
  - Run the terminal or command prompt as an administrator if necessary.

- **Plot Display Issues:**

  - If plots are not displaying, ensure that the scripts are saving the figures correctly.
  - Check that `matplotlib` and `seaborn` are properly installed and updated.

- **Dependency Issues:**

  - Ensure your installed packages match the versions specified in `requirements.txt`.
  - Here's the list of required packages with versions:

    ```plaintext
    certifi==2024.8.30
    charset-normalizer==3.4.0
    contourpy==1.3.0
    cycler==0.12.1
    fonttools==4.54.1
    idna==3.10
    kiwisolver==1.4.7
    matplotlib==3.9.2
    numpy==2.1.3
    packaging==24.1
    pandas==2.2.3
    pillow==11.0.0
    pyparsing==3.2.0
    python-dateutil==2.9.0.post0
    python-dotenv==1.0.1
    pytz==2024.2
    requests==2.32.3
    seaborn==0.13.2
    six==1.16.0
    tzdata==2024.2
    urllib3==2.2.3
    ```

  - To install these exact versions, you can update your `requirements.txt` file and run:

    ```bash
    pip install -r requirements.txt
    ```

---

## Conclusion

This project demonstrates a range of data analysis techniques across different domains, including API interaction, data cleaning, statistical analysis, and data visualization. By following this guide, you can replicate the analyses, explore the datasets, and gain insights into the data processing workflows.

---

## Acknowledgments

- **Lee Pettigrew** (Student Number: x20730039): Author of the project.
- **NASA API**: Provides access to APOD data.
- **Iris Dataset**: A classic dataset in machine learning and statistics.
- **Python Libraries**:

  - **pandas**: Data manipulation and analysis.
  - **NumPy**: Numerical computing.
  - **seaborn** and **matplotlib**: Data visualization.
  - **requests**: HTTP library for API calls.
  - **python-dotenv**: For managing environment variables.

---

For any questions or feedback, please contact **Lee Pettigrew**.

*Thank you for exploring the Data Analysis Project!*

---
