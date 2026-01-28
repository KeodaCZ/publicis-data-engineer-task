import os
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()

# Sensitive credentials
SAS_TOKEN = os.getenv("AZURE_SAS_TOKEN")

# Dataset URLs (without SAS token)
PLAN_URL = "https://detask.blob.core.windows.net/de-task/1AHA810_plan.csv"
POSTBUY_URL = "https://detask.blob.core.windows.net/de-task/1AHA810_postbuy.csv"