from logs.logger import logger
from utils.validators import assert_status_code, assert_json_keys, assert_json_values


# @pytest.mark.skip(reason="This API is deprecated")
def test_get_job_by_id(api_design_manager):
    logger.info("Starting test: test_get_job_by_id")
    endpoint = "job/JobByJobId/1"
    response = api_design_manager.get(endpoint)

    try:
        assert_status_code(response, 200)
        logger.info("Status code is 200 as expected.")
        logger.debug(f"Received response: {response.status_code} - {response.text}")

        assert_json_keys(response, ["created_by"])
        logger.info("'created_by' key found in the response.")

        assert_json_values(response, ("job_type_nm", "ingestion"))
        logger.info("Verified 'job_type_nm' key value is 'ingestion'.")

    except AssertionError as e:
        logger.error(f"Test failed due to assertion error: {e}")
        raise

    logger.info("Completed test: test_get_job_by_id")
