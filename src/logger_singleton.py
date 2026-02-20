import logging

class LoggerSingleton:
    _instance = None

    def __new__(cls):
        if LoggerSingleton._instance is None:
            obj = super().__new__(cls)
            obj.logger = logging.getLogger(__name__)
            logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='info.log', level=logging.INFO)
            LoggerSingleton._instance = obj
            LoggerSingleton.info(f"Created a new {cls.__name__} object")
        return LoggerSingleton._instance

    def info(message):
        singleton = LoggerSingleton()
        logger = singleton._instance.logger
        logger.info(f"(INFO): {message}")

    def warn(message):
        singleton = LoggerSingleton()
        logger = singleton._instance.logger
        logger.info(f"(WARN): {message}")
