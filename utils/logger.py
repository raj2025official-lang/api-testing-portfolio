import logging


def get_logger():
    logger = logging.getLogger("QA_Automation")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler("reports/test.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger