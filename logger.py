import logging
import time

class Logger:

    def __init__(self):

        logging.basicConfig(filename='info.log',
                            encoding='utf-8',
                            filemode='a',
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.packages_sent = 0
        self.start_time = time.time()
        logging.info('Application running.\n')

    def data_sent(self, message):
        logging.info('data package with following payload: ' + message + '\n')
        self.packages_sent += 1

    def paused(self):
        uptime = time.time() - self.start_time
        logging.info(f'Application paused   uptime: {uptime}s   packages sent: {self.packages_sent}\n')

        self.packages_sent = 0

    def resumed(self):
        self.start_time = time.time()
        logging.info('Application resumed.\n')

    def not_implemented(self):
        logging.info('real sensor was selected, not implemented.\n')
