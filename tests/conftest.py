import pytest
import sys
import os

from utils.api_client import APIClient
from config.env_handler import get_config

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(scope="session")
def api():
    config = get_config()
    return APIClient(
        base_url=config['base_url'],
        auth_token=config.get('auth_token')
    )
