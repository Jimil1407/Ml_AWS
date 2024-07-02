import logging
import os
from datetime import datetime

log_file  = f"{datetime.now().strftime ('%m-%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(logs_path,exist_ok=True)

log_file_path = os.path.join(logs_path,log_file)

logging.basicConfig(filename=log_file_path,
                    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO,                
                    )

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__=="__main__":
    logger = get_logger(__name__)
    logger.info("This is a test log message")