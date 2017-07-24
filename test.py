from Framework.vagrant_logger import Logger
from subprocess import Popen, PIPE

# FILENAME = os.path.basename(__file__)

# logger = Logger(file_id=FILENAME)


def vagrant_up():
    """
    Create a vagrant machine
    """
    try:
        sp = Popen("vagrant up", shell=True, stdout=PIPE, stderr=PIPE)
        logger.info("Spawning vagrant machines ...")

        stdout, stderr = sp.communicate()
        logger.info(stdout)

        if stderr:
            raise Exception(stderr)

        return

    except Exception as err:
        logger.error(
            "Couldn't bring up the machine/machines\
             due to error: %s" % (err))


vagrant_up()

logger = Logger(file_id="tc1")
logger.info("file is what it looks")
