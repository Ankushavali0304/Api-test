###########################################################
# method name: assert_status_code
# parameters: response, expected
# Desc:  Asserts the status code
############################################################
def assert_status_code(response, expected):
    assert response.status_code == expected, f"Expected {expected}, got {response.status_code}"


###########################################################
# method name: assert_json_keys
# parameters: response, key
# Desc:  Asserts that a key exists anywhere within the response JSON structure.
############################################################
def assert_json_keys(response, keys):
    """
    Assert that all specified keys exist in the JSON response, recursively.

    :param response: The response object from the API.
    :param keys: A single key (str) or list of keys (list of str) to verify in the JSON response.
    """
    if isinstance(keys, str):
        keys = [keys]  # Convert single key to list

    json_data = response.json()

    def recursive_search(data, key):
        if isinstance(data, dict):
            if key in data:
                return True
            return any(recursive_search(value, key) for value in data.values())
        elif isinstance(data, list):
            return any(recursive_search(item, key) for item in data)
        return False

    for key in keys:
        assert recursive_search(json_data, key), f"Key '{key}' not found in the response JSON."


###########################################################
# method name: assert_json_values
# parameters: response,expected_value
# Desc: Asserts that a key exists and has the expected value anywhere within the response JSON structure.
############################################################
def assert_json_values(response, expected_data):
    json_data = response.json()

    def recursive_search(data, key, expected_value):
        if isinstance(data, dict):
            if key in data and data[key] == expected_value:
                return True
            for value in data.values():
                if recursive_search(value, key, expected_value):
                    return True
        elif isinstance(data, list):
            for item in data:
                if recursive_search(item, key, expected_value):
                    return True
        return False

    if isinstance(expected_data, tuple) and len(expected_data) == 2:
        expected_data = {expected_data[0]: expected_data[1]}

    assert isinstance(expected_data, dict), "Expected data must be a dictionary or a key-value tuple."

    for key, expected_value in expected_data.items():
        assert recursive_search(json_data, key, expected_value), (
            f"Key '{key}' with value '{expected_value}' not found in the response JSON."
        )
