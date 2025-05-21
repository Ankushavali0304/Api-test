import pytest
import sys
import os
from dotenv import load_dotenv
from utils.api_client import APIClient
from config.env_handler import load_service_urls

# Add the root project directory to the sys.path to ensure utils is found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load environment variables from .env
load_dotenv()

# Initialize the base URLs at the start
load_service_urls()

# Fetch the auth token from the environment
AUTH_TOKEN = os.getenv("AUTH_TOKEN")


def get_api_client(service_key):
    return APIClient(service_name=service_key, auth_token=AUTH_TOKEN)


@pytest.fixture(scope="session")
def api():
    return get_api_client("interaction_manager")


@pytest.fixture(scope="session")
def api_job_executor():
    return get_api_client("job_executor")


@pytest.fixture(scope="session")
def api_metadata_service():
    return get_api_client("metadata_service")


@pytest.fixture(scope="session")
def api_design_manager():
    return get_api_client("design_manager")
