import inspect
import logging


def custom_logger(log_level):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(f"logs/{logger_name}.log", mode="w")
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                  datefmt='%d/%m/%Y %H:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def delete_logs_after_execution():

