import os
from dotenv import load_dotenv
from utils.api_client import APIClient

# Load environment variables from .env file
load_dotenv()


def load_service_urls():
    """Loads base URLs from .env and updates APIClient's BASE_URLS"""
    APIClient.BASE_URLS["interaction_manager"] = os.getenv("BASE_URL")
    APIClient.BASE_URLS["job_executor"] = os.getenv("BASE_URL1")
    APIClient.BASE_URLS["metadata_service"] = os.getenv("BASE_URL2")
    APIClient.BASE_URLS["design_manager"] = os.getenv("BASE_URL3")
