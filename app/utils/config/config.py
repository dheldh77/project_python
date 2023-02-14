import argparse
import configparser


class Configuration:
    ENV = {

    }

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls._instance = super().__new__(cls)
            cls._instance.init()
        return cls._instance

    def __del__(self):
        pass

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date

    @property
    def env(self):
        return self.__env

    @property
    def search_path(self):
        return self.__search_path

    @property
    def log_dir(self):
        return self.__log_dir

    def init(self):
        args, config = Parser().set_arguments()
        self.__start_date = args["start_date"]
        self.__end_date = args["end_date"]
        self.__env = args["env"].upper()
        self.__search_path = config[self.__env]["search_path"]
        self.__log_dir = config["Paths"]["log_dir"]


class Parser:
    __ARGUMENTS = [
        "--start_date",
        "--end_date",
        "--env"
    ]

    def set_arguments(self):
        args = self.__set_input_arguments()
        config = self.__set_configuration()
        return args, config

    def __set_input_arguments(self):
        parser = argparse.ArgumentParser(
            prog = 'ProgramName',
            description = 'What the program does',
            epilog = 'Text at the bottom of help'
        )
        [parser.add_argument(arg) for arg in self.__ARGUMENTS]
        return parser.parse_args().__dict__

    def __set_configuration(self):
        config = configparser.ConfigParser()
        config.read('env.ini')
        return config
        

if __name__ == "__main__":
    Parser.set_arguments()
        