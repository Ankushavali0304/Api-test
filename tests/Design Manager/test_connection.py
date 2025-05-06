from utils.validators import assert_status_code, assert_json_key, assert_json_value


def test_get_job_by_id(api):
    response = api.get("design-manager/api/v1/connection/getConnectionByConnectionId/3")
    assert_status_code(response, 200)
    assert_json_key(response, "status")
    assert_json_value(response, "name", "Snowflake Connection -Test")