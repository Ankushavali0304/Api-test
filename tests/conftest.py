import pytest
import sys
import os
from utils.api_client import APIClient
from config.env_handler import get_config, load_service_urls

# Add root path to allow absolute imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Call load_service_urls to initialize the base URLs at the start
load_service_urls()


@pytest.fixture(scope="session")
def api():
    """API client for base_url (interaction_manager service)."""
    config = get_config()
    return APIClient(service_name="interaction_manager", auth_token=config.get("auth_token"))


@pytest.fixture(scope="session")
def api_job_executor():
    """API client for base_url1 (job_executor service)."""
    config = get_config()
    return APIClient(service_name="job_executor", auth_token=config.get("auth_token"))


@pytest.fixture(scope="session")
def api_metadata_service():
    """API client for base_url2 (metadata-service)."""
    config = get_config()
    return APIClient(service_name="metadata_service", auth_token=config.get("auth_token"))


@pytest.fixture(scope="session")
def api_design_manager():
    """API client for base_url3 (design_manager)."""
    config = get_config()
    return APIClient(service_name="design_manager", auth_token=config.get("auth_token"))
