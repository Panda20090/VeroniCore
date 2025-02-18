# logging.py
# This script sets up a logging system for the VeroniCore project.
# It provides functionality to log different levels of messages (info, warning, error) to a file and optionally to the console.

import logging
import os

class Logger:
    def __init__(self, name='VeroniCoreLogger', log_file='VeroniCore.log', log_level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # Create file handler
        self.log_file = log_file
        if not os.path.exists(os.path.dirname(log_file)):
            os.makedirs(os.path.dirname(log_file))
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger

# Example usage of the Logger class
if __name__ == "__main__":
    # Initialize logger
    logger = Logger().get_logger()

    # Log messages
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
