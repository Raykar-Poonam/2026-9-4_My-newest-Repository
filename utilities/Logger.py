import logging
import inspect

class Loggen:

    @staticmethod
    def log_generator():

        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)
        log_file = logging.FileHandler("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Logs\\test_login_TC01.log")
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        log_file.setFormatter(log_format)
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger