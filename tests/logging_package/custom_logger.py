import inspect
import logging
import os
import pathlib
import shutil


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
    return logger, file_handler


def delete_logs_after_execution():
    path = pathlib.Path("D:/repositories/selenium/tests/logging_package/logs")
    list_files = os.listdir(path)
    for element in list_files:
        if element[-4:] == ".log":
            try:
                os.remove(pathlib.Path(f"{path}/{element}"))
            except OSError as oe:
                print(f"Error: {oe} file deletion failed.")
        else:
            print(f"Element: {element} is not finished with .log extension.")

    #
    #files = [os.remove(pathlib.Path(f"{path}/{element}")) for element in list_files if element[-4:] == ".log"]






