import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler("cookiecutter_setup.log"), logging.StreamHandler(sys.stdout)],
    )
    logger = logging.getLogger(__name__)
    return logger