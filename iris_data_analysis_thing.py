import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_inspect_data(csv_file='iris.csv'):
    """
    Loads the iris dataset from a CSV file and inspects its basic properties.

    Parameters:
    - csv_file (str): Path to the iris CSV file.

    Returns:
    - df (DataFrame): Loaded pandas DataFrame.
    """
    try:
        # Read the iris.csv file into a DataFrame
        df = pd.read_csv(csv_file)
        print("Successfully loaded 'iris.csv' into a DataFrame.\n")

        # a. Number of data points
        num_data_points = df.shape[0]
        print(f"Number of data points: {num_data_points}\n")

        # b. Data types of the columns
        print("Data types of the columns:")
        print(df.dtypes, "\n")

        # c. Column names
        column_names = df.columns.tolist()
        print("Column names:")
        print(column_names, "\n")

        # d. Number of species
        unique_species = df['Species'].unique()
        num_species = unique_species.size
        print(f"Number of species: {num_species}")
        print("Species included in the data:")
        print(unique_species, "\n")

        return df
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The CSV file is corrupt or improperly formatted.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def correct_data_errors(df):
    """
    Corrects errors in the 35th and 38th rows of the DataFrame.

    Parameters:
    - df (DataFrame): The pandas DataFrame to correct.

    Returns:
    - df (DataFrame): The corrected DataFrame.
    """
    try:
        # Display original 35th and 38th rows (1-indexed)
        print("Original 35th row:")
        print(df.iloc[34], "\n")

        print("Original 38th row:")
        print(df.iloc[37], "\n")

        # Correct the 35th row
        df.iloc[34] = [4.9, 3.1, 1.5, 0.2, 'setosa']

        # Correct the 38th row
        df.iloc[37] = [4.9, 3.6, 1.4, 0.1, 'setosa']

        # Display corrected rows
        print("Corrected 35th row:")
        print(df.iloc[34], "\n")

        print("Corrected 38th row:")
        print(df.iloc[37], "\n")

        return df
    except IndexError:
        print("Error: The DataFrame does not have enough rows to correct.")
        return df
    except Exception as e:
        print(f"An unexpected error occurred while correcting data: {e}")
        return df

def add_new_features(df):
    """
    Adds 'Petal Ratio' and 'Sepal Ratio' features to the DataFrame.

    Parameters:
    - df (DataFrame): The pandas DataFrame to modify.

    Returns:
    - df (DataFrame): The modified DataFrame with new features.
    """
    try:
        # Calculate Petal Ratio (Petal.Length / Petal.Width)
        df['Petal Ratio'] = df['Petal.Length'] / df['Petal.Width']

        # Calculate Sepal Ratio (Sepal.Length / Sepal.Width)
        df['Sepal Ratio'] = df['Sepal.Length'] / df['Sepal.Width']

        print("Added 'Petal Ratio' and 'Sepal Ratio' to the DataFrame.\n")
        return df
    except ZeroDivisionError:
        print("Error: Division by zero encountered while calculating ratios.")
        return df
    except Exception as e:
        print(f"An unexpected error occurred while adding new features: {e}")
        return df

def save_corrected_data(df, output_file='iris_corrected.csv'):
    """
    Saves the corrected DataFrame to a CSV file.

    Parameters:
    - df (DataFrame): The pandas DataFrame to save.
    - output_file (str): The filename for the corrected CSV.
    """
    try:
        df.to_csv(output_file, index=False)
        print(f"Modified DataFrame saved as '{output_file}'.\n")
    except PermissionError:
        print(f"Error: Permission denied when writing to '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred while saving the DataFrame: {e}")

def calculate_correlations(df):
    """
    Calculates pairwise correlations between all numeric columns and identifies
    the highest positive and negative correlations.

    Parameters:
    - df (DataFrame): The pandas DataFrame to analyze.

    Returns:
    - correlation_matrix (DataFrame): The pairwise correlation matrix.
    """
    try:
        # Select numeric columns
        numeric_cols = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Petal Ratio', 'Sepal Ratio']

        # Calculate the correlation matrix
        correlation_matrix = df[numeric_cols].corr()

        print("Pairwise correlation matrix:")
        print(correlation_matrix, "\n")

        # Unstack the correlation matrix to a Series
        corr_unstacked = correlation_matrix.unstack()

        # Remove self-correlations
        corr_unstacked = corr_unstacked[corr_unstacked < 1]

        # Find the highest positive correlation
        highest_positive = corr_unstacked.idxmax()
        highest_positive_value = corr_unstacked.max()
        print(f"Highest positive correlation is between {highest_positive} with a correlation of {highest_positive_value:.2f}")

        # Find the highest negative correlation
        highest_negative = corr_unstacked.idxmin()
        highest_negative_value = corr_unstacked.min()
        print(f"Highest negative correlation is between {highest_negative} with a correlation of {highest_negative_value:.2f}\n")

        # Interpretation
        print("Interpretation:")
        print(f"- The highest positive correlation between {highest_positive} indicates a strong direct relationship.")
        print(f"- The highest negative correlation between {highest_negative} indicates a strong inverse relationship.\n")

        return correlation_matrix
    except KeyError:
        print("Error: One or more specified columns are not in the DataFrame.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while calculating correlations: {e}")
        return None

def create_scatter_plot_with_regression(df, output_file='iris_scatter_with_regression.pdf'):
    """
    Creates a scatter plot with Sepal Ratio on the x-axis and Petal Ratio on the y-axis,
    colored by species, and adds a linear regression line for each species.

    Parameters:
    - df (DataFrame): The pandas DataFrame to plot.
    - output_file (str): The filename for the saved plot.
    """
    try:
        # Set the aesthetic style of the plots
        sns.set(style="whitegrid")

        # Create the scatter plot with regression lines
        sns.lmplot(
            x='Sepal Ratio',
            y='Petal Ratio',
            hue='Species',
            data=df,
            height=6,
            aspect=1.5,
            markers=['o', 's', 'D'],
            scatter_kws={'s': 50, 'alpha': 0.7},
            ci=None
        )

        # Set plot title and labels
        plt.title('Scatter Plot of Sepal Ratio vs. Petal Ratio with Regression Lines')
        plt.xlabel('Sepal Ratio (Sepal.Length / Sepal.Width)')
        plt.ylabel('Petal Ratio (Petal.Length / Petal.Width)')

        # Save the plot
        plt.savefig(output_file)
        plt.close()
        print(f"Scatter plot saved as '{output_file}'.\n")
    except KeyError as e:
        print(f"Error: Column not found in DataFrame: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while creating the scatter plot: {e}")

def create_pair_plot(df):
    """
    Creates a pair plot for the four original numeric features and the two new ratio features,
    colored by species.

    Parameters:
    - df (DataFrame): The pandas DataFrame to plot.
    """
    try:
        # Select the columns for the pair plot
        pairplot_cols = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Petal Ratio', 'Sepal Ratio']

        # Create the pair plot
        sns.pairplot(df[pairplot_cols + ['Species']], hue='Species', height=2.5, diag_kind='kde')

        # Adjust layout
        plt.tight_layout()

        # Save the pair plot as an image
        plt.savefig('iris_pair_plot.png')
        plt.close()
        print("Pair plot saved as 'iris_pair_plot.png'.\n")
    except KeyError as e:
        print(f"Error: Column not found in DataFrame: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while creating the pair plot: {e}")

def main():
    # Step 1: Load and inspect the data
    df = load_and_inspect_data('iris.csv')
    if df is None:
        return

    # Step 2: Correct data errors
    df = correct_data_errors(df)

    # Step 3: Add new features
    df = add_new_features(df)

    # Step 4: Save the corrected data
    save_corrected_data(df, 'iris_corrected.csv')

    # Step 5: Calculate pairwise correlations
    correlation_matrix = calculate_correlations(df)

    # Step 6: Create scatter plot with regression lines
    create_scatter_plot_with_regression(df, 'iris_scatter_with_regression.pdf')

    # Step 7: Create a pair plot
    create_pair_plot(df)

if __name__ == "__main__":
    main()
