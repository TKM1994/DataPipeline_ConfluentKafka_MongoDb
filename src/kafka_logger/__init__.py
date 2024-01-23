# Importing necessary libraries
import logging
from datetime import datetime
import os


LOG_DIR="logs"

# return log file name in desired format
def get_log_file_name():
    return f"log_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"



LOG_FILE_NAME=get_log_file_name()

# creating a log_directory named logs
os.makedirs(LOG_DIR,exist_ok=True)


# getting log file path from log_directory and file name
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)


# creating logging
logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)