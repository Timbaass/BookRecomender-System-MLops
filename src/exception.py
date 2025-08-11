import sys
import logging 
from logger import setup_logging

setup_logging()

def error_message_detail(error, error_detail: sys):
    """Extracts error message detail from the exception."""
    _ , _ , exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in Python Script Name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        logging.info(self.error_message)
        return self.error_message
    
if __name__ == "__main__":
    try:
        x = 1/0
    except Exception as e:
        raise CustomException(e, sys)