from logs.logger import logger
from utils.validators import assert_status_code, assert_json_keys, assert_json_values
from config.env_handler import load_service_urls
from utils.api_client import APIClient

# ✅ Populate BASE_URLS before anything else
load_service_urls()


def test_connection(api_design_manager):
    endpoint = "connection/getConnectionByConnectionId/3"

    url = f"{api_design_manager.base_url.rstrip('/')}/{endpoint}"  # Constructing the URL dynamically
    response = api_design_manager.get(endpoint)
    test_result = {
        "status_code": response.status_code,
        "response_json": None,
        "error": None,
        "environment_url": url
    }

    try:
        assert_status_code(response, 200)
        logger.info("Status code is 200 as expected.")

        json_data = response.json()
        test_result["response_json"] = json_data

        assert_json_keys(response, ["status"])
        logger.info("'status' key found in the response.")

        assert_json_values(response, ("name", "Snowflake Connection -Test"))
        logger.info("Verified 'name' key value is 'Snowflake Connection -Test'.")

    except AssertionError as e:
        logger.error(f"Test failed due to assertion error: {e}")
        raise

    return test_result


def run(api_design_manager):
    return test_connection(api_design_manager)
