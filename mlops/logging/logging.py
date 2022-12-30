import logging
import sys


def init():
    """Setup a logger object."""
    root = logging.getLogger()
    if not root.hasHandlers():
        # set level and format
        root.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s [%(name)s] [%(levelname)s] %(message)s", datefmt="%H:%M:%S"
        )

        # output in console
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        root.addHandler(ch)

        root.info("Root didn't have handlers, set up now. ")
    else:
        root.info("Root already had handlers. ")


def get(name):
    """Get the already initialized logger."""
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    return log


if __name__ == "__main__":
    get(__name__)
