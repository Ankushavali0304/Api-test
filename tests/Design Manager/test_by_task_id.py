from utils.validators import assert_status_code, assert_json_keys, assert_json_values
from logs.logger import logger


def test_get_job_by_id(api_design_manager):

    endpoint = "job/TaskColumnByTaskId/1"

    response = api_design_manager.get(endpoint)

    try:
        assert_status_code(response, 200)
        logger.info("Status code is 200 as expected.")

        assert_json_keys(response, ["created_by"])
        assert_json_values(response, ("task_id", 1))
    except AssertionError as e:
        logger.error(f"Test failed due to assertion error: {e}")
        raise