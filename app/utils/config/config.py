import argparse
import configparser


class Configuration:
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

    def init(self):
        args, config = Parser().set_arguments()
        self.__start_date = args["start_date"]
        self.__end_date = args["end_date"]
        self.__env = args["env"]
        self.__search_path = config["search_path"]


class Parser:
    __ARGUMENTS = [
        "--start_date",
        "--end_date",
        "--env"
    ]

    def set_arguments(self):
        args = self.__set_input_arguments()
        config = self.__set_configuration(args.env)
        return args.__dict__, dict(config)

    def __set_input_arguments(self):
        parser = argparse.ArgumentParser(
            prog = 'ProgramName',
            description = 'What the program does',
            epilog = 'Text at the bottom of help'
        )
        [parser.add_argument(arg) for arg in self.__ARGUMENTS]
        return parser.parse_args()

    def __set_configuration(self, env):
        config = configparser.ConfigParser()
        config.read('env.ini')
        return config[env.upper()]
        

if __name__ == "__main__":
    Parser.set_arguments()
        