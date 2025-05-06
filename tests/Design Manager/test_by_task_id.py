from utils.validators import assert_status_code, assert_json_keys, assert_json_values
from logs.logger import logger


def test_get_job_by_id(api):
    response = api.get("design-manager/api/v1/job/TaskColumnByTaskId/1")

    try:
        assert_status_code(response, 200)
        logger.info("Status code is 200 as expected.")

        assert_json_keys(response, ["created_by"])
        assert_json_values(response, ("task_id", 1))
    except AssertionError as e:
        logger.error(f"Test failed due to assertion error: {e}")
        raise