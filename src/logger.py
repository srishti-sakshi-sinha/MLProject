#files for logging the files. logs and timestamps.

import logging
import os
from datetime import datetime

#creating a log file which will contain datetime in the specified manner

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)            
#it is created in the src folder because all the files are in this file and the log is maintained with respect to the current working directory.
os.makedirs(logs_path,exist_ok=True)        #this means even if the file is already created/exists, append it anyway in the logs file.


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#TO CREATE AND OVERWRITE THE LOG FILES, WE USE basicConfig

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)


#to check if the file is successfully running or not we can do this

if __name__=='__main__':
    logging.info("Logging has started")