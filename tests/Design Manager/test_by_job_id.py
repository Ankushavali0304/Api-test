import pytest
from logs.logger import logger
from utils.validators import assert_status_code, assert_json_keys, assert_json_values


# @pytest.mark.skip(reason="This API is deprecated")
def test_get_job_by_id(api):
    logger.info("Starting test: test_get_job_by_id")

    response = api.get("design-manager/api/v1/job/JobByJobId/1")
    logger.debug(f"Received response: {response.status_code} - {response.text}")

    try:
        assert_status_code(response, 200)
        logger.info("Status code is 200 as expected.")

        assert_json_keys(response, ["created_by"])
        logger.info("'created_by' key found in the response.")

        assert_json_values(response, ("job_type_nm", "ingestion"))
        logger.info("Verified 'job_type_nm' key value is 'ingestion'.")

    except AssertionError as e:
        logger.error(f"Test failed due to assertion error: {e}")
        raise

    logger.info("Completed test: test_get_job_by_id")
