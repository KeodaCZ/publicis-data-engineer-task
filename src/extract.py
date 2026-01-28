import pandas as pd
from config import PLAN_URL, POSTBUY_URL, SAS_TOKEN


def load_csv_from_azure(url: str) -> pd.DataFrame:
    """
    Load CSV file from Azure Blob Storage using SAS token.
    """
    if SAS_TOKEN is None:
        raise ValueError("SAS token not found. Check your .env file.")

    full_url = f"{url}?{SAS_TOKEN}"
    df = pd.read_csv(full_url)

    return df


def load_plan_data() -> pd.DataFrame:
    return load_csv_from_azure(PLAN_URL)


def load_postbuy_data() -> pd.DataFrame:
    return load_csv_from_azure(POSTBUY_URL)