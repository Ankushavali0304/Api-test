from utils.api_client import APIClient
from utils.validators import assert_status_code, assert_json_keys, assert_json_values
from logs.logger import logger


def test_get_user(api):  # Using fixture for job_executor service
    login_payload = {
        "username": "john.doe@example.com",
        "password": "welcome2024"
    }
    endpoint = "user/login"
    response = api.post(endpoint, json=login_payload)  # Making API request with job_executor base_url
    url = f"{api.base_url.rstrip('/')}{endpoint}"  # Constructing the URL dynamically
    try:
        assert_status_code(response, 200)
        logger.info(f"API call to {url} successful.")
        logger.debug(f"Response status: {response.status_code}, Body: {response.text}")

        # Validating the JSON response
        assert_json_keys(response, ["first_nm", "last_nm"])
        assert_json_values(response, ("first_nm", "John"))

    except AssertionError as e:
        logger.error(f"Test failed due to assertion error: {e}")
        raise
