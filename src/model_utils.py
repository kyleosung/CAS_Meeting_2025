import os
import pickle
from typing import Any


def pickle_sk_model(
    model: Any, filename: str, overwrite_if_exists: bool = False
) -> None:
    """
    Save a scikit-learn model to a file using pickle.

    Parameters
    ----------
    model
        The scikit-learn model to save.
    filename
        The name of the file to save the model to.
    """

    if os.path.exists(filename) and not overwrite_if_exists:
        raise ValueError(
            f"File {filename} already exists. Use `overwrite_if_exists=True` to overwrite."
        )

    with open(filename, "wb") as file:
        pickle.dump(model, file)
    print(f"Model saved to {filename}.")


def unpickle_sk_model(filename: str) -> Any:
    """
    Load a scikit-learn model from a file using pickle.

    Parameters
    ----------
    filename
        The name of the file to load the model from.

    Returns
    -------
    model
        The loaded scikit-learn model.

    """
    assert os.path.exists(filename), f"File {filename} does not exist."

    with open(filename, "rb") as file:
        model = pickle.load(file)

    return model
