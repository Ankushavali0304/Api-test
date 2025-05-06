import time


def retry_request(func, retries=3, delay=2):
    for _ in range(retries):
        response = func()
        if response.status_code == 200:
            return response
        time.sleep(delay)
    return response
