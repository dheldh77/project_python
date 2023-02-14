import logging


class Logger(object):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        self.__logger = logging.getLogger()
        self.__logger.setLevel(logging.INFO)

        # log 출력 형식
        formatter = logging.Formatter('[%(levelname)s] :: %(asctime)s :: %(message)s')

        # log 출력
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.__logger.addHandler(stream_handler)

        # log를 파일에 출력
        file_handler = logging.FileHandler('my.log')
        file_handler.setFormatter(formatter)
        self.__logger.addHandler(file_handler)
    
    def info(self, msg):
        self.__logger.info(msg)

    @property
    def logger(self):
        return self.__logger