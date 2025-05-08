from logs.logger import logger
from utils.validators import assert_status_code, assert_json_keys, assert_json_values


def test_get_job_by_id(api_design_manager):

    endpoint = "connection/getConnectionByConnectionId/3"

    response = api_design_manager.get(endpoint)

    try:
        assert_status_code(response, 200)
        logger.info("Status code is 200 as expected.")

        assert_json_keys(response, ["status"])
        logger.info("'status' key found in the response.")

        assert_json_values(response, ("name", "Snowflake Connection -Test"))
        logger.info("Verified 'name' key value is 'Snowflake Connection -Test'.")

    except AssertionError as e:
        logger.error(f"Test failed due to assertion error: {e}")
        raise


