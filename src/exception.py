#file for all the exception handelling

import sys


#for error message details

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()          #this will give information about the error found.
    file_name=exc_tb.tb_frame.f_code.co_filename        #this will give the information of the file where errror has occured
    error_message="Error has occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno,str(error)
        )
    
    return error_message

#creating custom exception class

class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message