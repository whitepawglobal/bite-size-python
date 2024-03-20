import logging
import os

logfilepath = "log.txt"

logging.basicConfig(filename = logfilepath, 
            level = os.environ.get("LOGLEVEL", "INFO").upper(),
            format = '%(asctime)s %(levelname)s %(filename)s:%(lineno)s : %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S') 

#https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
logging.getLogger().addHandler(logging.StreamHandler())

if __name__ == "__main__":

    for i in range(5):

        logging.info(f"Iteration {i}")

    