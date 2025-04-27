import pandas as pd

from src.constants import INITIAL_FILE_PATH


def load_dataframe(file_path: str = INITIAL_FILE_PATH) -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file. Defaults to INITIAL_FILE_PATH.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}. Please check the path.")
        return pd.DataFrame()  # Returns empty DataFrame on error
