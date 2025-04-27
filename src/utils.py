import pandas as pd

from src.constants import ORIGINAL_DATASET


def load_dataframe(file_path: str = ORIGINAL_DATASET) -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters
    ----------
        file_path : str
            The path to the CSV file. Defaults to src.constants.ORIGINAL_DATASET.

    Returns
    -------
        pd.DataFrame
            The loaded DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}. Please check the path.")
        return pd.DataFrame()  # Returns empty DataFrame on error
