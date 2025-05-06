import logging
import os

# Create a logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Create a custom logger
logger = logging.getLogger(__name__)

# Set the default logging level (INFO, DEBUG, WARNING, ERROR, CRITICAL)
logger.setLevel(logging.DEBUG)

# Create file handler for logging to a file
log_file = os.path.join('logs', 'api_test.log')
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create a console handler for logging to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a log formatter and set it for both handlers
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(log_format)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Test log entries (you can remove this part later)
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

# To log the request or response in API tests, you can use the logger like this:
# logger.info(f"Making API request to {url}")
# logger.error(f"API request failed with status code {response.status_code}")

# In your API tests, you can now use the `logger` to log various events.
