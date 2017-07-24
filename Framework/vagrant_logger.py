import logmatic
import logging
import socket
import logging.handlers
import datetime
import os

# Constants:
LOG_ROOT = os.path.join(os.path.dirname(__file__), 'LOGS')


class Logger(object):

    def __init__(self, logger=None, date_tag=None, filehandler=None,
                 consolehandler=None, file_id=None):

        if date_tag is None:
            dateTag = datetime.datetime.now()\
                .strftime("%Y:%b:%d-%H:%M:%S")

        if file_id is None:
            file_id = file_id

        if logger is None:
            logger = logging.getLogger(file_id)
            # Add handlers and set log level

        if filehandler is None:
            logname = '_'.join([str(file_id), dateTag, '.json'])
            if not os.path.exists(LOG_ROOT):
                os.makedirs(LOG_ROOT)
            filehandler = logging.FileHandler(
                os.path.join(LOG_ROOT, logname))
            filehandler.setFormatter(logmatic.JsonFormatter(
                extra={"hostname": socket.gethostname()}))

        if consolehandler is None:
            consolehandler = logging.StreamHandler()
            consolehandler.setFormatter(logmatic.JsonFormatter(
                extra={"hostname": socket.gethostname()}))

        logger.addHandler(filehandler)
        logger.addHandler(consolehandler)
        logger.setLevel(logging.DEBUG)

        self.logger = logger
        self.info = logger.info
        self.debug = logger.debug
        self.dateTag = dateTag
        self.filehandler = filehandler
        self.consolehandler = consolehandler
        self.file_id = file_id

    def info(self, message):
        return self.logger.info(message)

    def debug(self, message):
        return self.logger.debug(message)

    def error(self, message):
        return self.logger.error(message)


if __name__ == '__main__':

    log = Logger()
    log.info("anupam")
    # log.info("debnath")
