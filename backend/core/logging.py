# Import Python's built-in logging module
import logging


# Function to configure and initialize the logger
def setup_logger():

    # Create or get a logger with the name "ai_code_review"
    # This name helps identify logs from this application
    logger = logging.getLogger("ai_code_review")

    # Set the logging level to INFO
    # This means INFO, WARNING, ERROR, and CRITICAL messages will be recorded
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers if logger is initialized again
    # Without this check, duplicate log messages may appear
    if not logger.handlers:

        # Define the format of log messages
        # Example output:
        # 2026-03-04 11:07:30 - INFO - ai_code_review - Received code review request
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        # Create a console handler to display logs in the terminal
        console_handler = logging.StreamHandler()

        # Apply the defined format to the console handler
        console_handler.setFormatter(formatter)

        # Attach the console handler to the logger
        logger.addHandler(console_handler)

    # Return the configured logger instance
    return logger


# Initialize the logger when this file is imported
# Other modules can directly use: from core.logging import logger
logger = setup_logger()