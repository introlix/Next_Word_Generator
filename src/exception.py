import sys
from src.logger import logging

def error_message_details(error, error_detail: sys):
    _, _, exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    line_number = exec_tb.tb_lineno
    error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}] error message: [{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
        
# if __name__ == '__main__':
#     try:
#         x = 1
#         print(x/0)
#     except Exception as e:
#         logging.info(e)
#         raise CustomException(e, sys)