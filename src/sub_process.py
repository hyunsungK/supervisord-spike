import os 
import logging
import time

from multiprocessing import Process

logger = logging.getLogger(__name__)


def doubler():
    while True:
        logger.error('child process is running...')
        time.sleep(2)
    

if __name__ == '__main__':
    proc = Process(target=doubler)
    proc.start()

    proc.join()