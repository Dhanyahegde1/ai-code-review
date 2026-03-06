import logging


# Function to configure and initialize the logger
def setup_logger():

    
    logger = logging.getLogger("ai_code_review")
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers
  
    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger

# Initialize the logger when this file is imported

logger = setup_logger()