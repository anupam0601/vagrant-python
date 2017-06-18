import logmatic
import logging
import socket
import logging.handlers
import datetime
import os

# Constants:

FILENAME = os.path.basename(__file__)


class Logger(object):

    def __init__(self, logger=None, date_tag=None, filehandler=None,
                 consolehandler=None, file_id=None,):

        if file_id is None:
            file_id = file_id

        if logger is None:
            logger = logging.getLogger(file_id)
            # Add handlers and set log level

        if date_tag is None:
            dateTag = datetime.datetime.now()\
                .strftime("%Y:%b:%d-%H:%M:%S")

        if filehandler is None:
            filehandler = logging.FileHandler(
                ('%s_%s.json') % (file_id, dateTag))
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
