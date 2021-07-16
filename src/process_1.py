import logging
import time

logger = logging.getLogger(__name__)


class Process1:
    def __init__(self):
        pass

    def run(self):
        try:
            self._loop()
        except Exception as e:
            logger.exception('Unexpected error')

    def _loop(self):
        while True:
            logger.error('Process1 is running...')
            time.sleep(2)


if __name__ == "__main__":
    worker = Process1()
    worker.run()
