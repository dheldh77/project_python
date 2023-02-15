import logging
import os
import sys
from multiprocessing import current_process


class Logger(object):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance.init()
        return cls._instance

    def __set_path(self):
        log_dir = "log"
        pid = "main" if current_process().name.lower() == "mainprocess" else current_process().name[-1]
        filename = "test.log"
        
        os.makedirs(f"{log_dir}/{pid}", exist_ok=True)
        self.__path = f"{log_dir}/{pid}/{filename}"

    def init(self):
        self.__set_path()
        self.__logger = logging.getLogger()
        self.__logger.setLevel(logging.INFO)

        # log 출력 형식
        formatter = logging.Formatter('[%(levelname)s] :: %(asctime)s :: %(message)s')

        # log 출력
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.__logger.addHandler(stream_handler)

        # log를 파일에 출력
        file_handler = logging.FileHandler(self.__path)
        file_handler.setFormatter(formatter)
        self.__logger.addHandler(file_handler)

    def __get_function_name(self):
        return sys._getframe(2).f_code.co_name

    def __get_class_name(self, cls):
        return str(cls).replace("<class '", "").replace("'>", "")
    
    def info(self, cls, msg=None):
        self.__logger.info(f"{self.__get_class_name(cls)}.{self.__get_function_name()} >> {msg}")

    @property
    def logger(self):
        return self.__logger