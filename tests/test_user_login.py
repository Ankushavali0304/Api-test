from utils.api_client import APIClient
from utils.validators import assert_status_code, assert_json_keys, assert_json_values
from logs.logger import logger
from config.env_handler import load_service_urls


# ✅ Populate BASE_URLS before anything else
load_service_urls()


def test_user_login(api):  # Accepts api instance (fixture or manually passed)
    login_payload = {
        "username": "john.doe@example.com",
        "password": "welcome2024"
    }
    endpoint = "user/login"
    url = f"{api.base_url.rstrip('/')}/{endpoint}"  # Constructing the URL dynamically
    response = api.post(endpoint, json=login_payload)  # Making API request with base_url
    test_result = {
        "status_code": response.status_code,
        "response_json": None,
        "error": None,
        "environment_url": url
    }
    try:
        assert_status_code(response, 200)
        logger.info(f"API call to {url} successful.")
        logger.debug(f"Response status: {response.status_code}, Body: {response.text}")

        json_data = response.json()
        test_result["response_json"] = json_data

        # Validating the JSON response
        assert_json_keys(response, ["first_nm", "last_nm"])
        assert_json_values(response, ("first_nm", "John"))

    except AssertionError as e:
        logger.error(f"Test failed due to assertion error: {e}")
        raise

    return test_result


# ✅ For test runner usage
def run(api):
    return test_user_login(api)

