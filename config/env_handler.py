import yaml
import os

from utils.api_client import APIClient


def get_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def load_service_urls():
    """Loads base URLs from config and updates APIClient's BASE_URLS"""
    config = get_config()
    APIClient.BASE_URLS["interaction_manager"] = config.get("base_url")
    APIClient.BASE_URLS["job_executor"] = config.get("base_url1")
    APIClient.BASE_URLS["metadata_service"] = config.get("base_url2")
    APIClient.BASE_URLS["design_manager"] = config.get("base_url3")

