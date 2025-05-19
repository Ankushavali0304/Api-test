from logs.logger import logger
from utils.api_client import APIClient
from utils.validators import assert_status_code, assert_json_keys, assert_json_values


def test_by_task_id(api_design_manager):
    endpoint = "job/TaskColumnByTaskId/1"
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
        logger.debug(f"Received response: {response.status_code} - {response.text}")

        json_data = response.json()
        test_result["response_json"] = json_data

        assert_json_keys(response, ["created_by"])
        logger.info("'created_by' key found in the response.")

        assert_json_values(response, ("task_id", 1))
        logger.info("Verified 'task_id' key value is '1'.")

    except AssertionError as e:
        logger.error(f"Test failed due to assertion error: {e}")
        test_result["error"] = str(e)

    logger.info("Completed test: test_by_task_id")
    return test_result


def run(api_design_manager):
    return test_by_task_id(api_design_manager)
