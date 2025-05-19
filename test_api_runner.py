import pytest
import traceback
import inspect
import sys
import json
import importlib.util
import os

from utils.api_client import APIClient
from utils.email import generate_email_report
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get the auth token from environment
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

# Shared results list to accumulate test results during the run
test_results = []

REPORT_DIR = os.path.join(os.path.dirname(__file__), "reports")
os.makedirs(REPORT_DIR, exist_ok=True)


# Fixture to provide API clients for tests
@pytest.fixture(scope="session")
def fixture_clients():
    return {
        "api": APIClient("interaction_manager", AUTH_TOKEN),
        "api_job_executor": APIClient("job_executor", AUTH_TOKEN),
        "api_design_manager": APIClient("design_manager", AUTH_TOKEN),
        "api_metadata_service": APIClient("metadata_service", AUTH_TOKEN),
    }


def run_test_func(test_func, fixture_clients):
    result = {
        "test_case": f"{test_func.__module__.removesuffix('.run')}.{test_func.__name__}",
        "status_code": "N/A",
        "result": "PASS",
        "response": "N/A",
        "environment_url": "N/A",
        "error_message": ""
    }

    try:
        required_args = inspect.signature(test_func).parameters
        args_to_pass = []

        for arg in required_args:
            if arg in fixture_clients:
                args_to_pass.append(fixture_clients[arg])

        response = test_func(*args_to_pass)

        if response is None:
            result["result"] = "FAIL"
            result["error_message"] = "Test returned None instead of a response."
        else:
            status_code = response.get("status_code", "N/A")
            result["status_code"] = status_code
            result["response"] = response.get("response_json", "N/A")
            result["error_message"] = response.get("error", "")
            result["environment_url"] = response.get("environment_url", "N/A")

            if not (200 <= int(status_code) < 300) or response.get("error"):
                result["result"] = "FAIL"

    except AssertionError as ae:
        result["result"] = "FAIL"
        result["error_message"] = str(ae)
    except Exception:
        result["result"] = "FAIL"
        result["error_message"] = traceback.format_exc()

    return result


def discover_test_functions():
    test_funcs = []
    root_dir = os.path.join(os.path.dirname(__file__), "tests")

    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.startswith("test_") and file.endswith(".py"):
                full_path = os.path.join(dirpath, file)
                rel_path = os.path.relpath(full_path, os.path.dirname(__file__))
                module_name = rel_path.replace(os.sep, ".").replace(".py", "")

                try:
                    spec = importlib.util.spec_from_file_location(module_name, full_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    if hasattr(module, "run") and callable(getattr(module, "run")):
                        test_funcs.append(getattr(module, "run"))
                except Exception as e:
                    print(f"⚠️ Failed to import {module_name}: {e}")

    return test_funcs


@pytest.mark.parametrize("test_func", discover_test_functions())
def test_run(test_func, fixture_clients):
    result = run_test_func(test_func, fixture_clients)
    test_results.append(result)

    with open("test_results.json", "w") as f:
        json.dump(test_results, f, indent=2)

    assert result["result"] == "PASS", (
        f"{result['test_case']} failed with status {result['status_code']}\n"
        f"Error: {result['error_message']}"
    )


import datetime


def main():
    """
    Main entry point: runs pytest on this file, then sends email report with results.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"api_test_email_report_{timestamp}.html"
    report_file = os.path.join(REPORT_DIR, report_filename)

    exit_code = pytest.main([
        "-s",
        __file__,
        f"--html={report_file}",
        "--self-contained-html"
    ])

    # Load test results for the email body
    try:
        with open("test_results.json", "r") as f:
            saved_results = json.load(f)
    except Exception as e:
        print("Could not load test results:", str(e))
        saved_results = []

    # Prepare email config
    email_config = {
        "sender": os.getenv("SMTP_SENDER"),
        "app_password": os.getenv("SMTP_PASSWORD"),
        "host": os.getenv("SMTP_HOST", "smtp.office365.com"),
        "port": int(os.getenv("SMTP_PORT", 587)),
        "recipient": [r.strip() for r in os.getenv("SMTP_RECIPIENT", "").split(",") if r.strip()],
    }

    try:
        generate_email_report(
            saved_results,
            send_email=True,
            email_config=email_config,
            html_attachment_path=report_file  # Pass timestamped report path
        )
    except Exception as e:
        print("Error generating email report:", str(e))

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
