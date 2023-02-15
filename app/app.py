from utils.logger.logger import Logger
from utils.config.config import Configuration
from executor import ExectorFactory


if __name__ == "__main__":
    logger = Logger()
    parser = Configuration()
    executor = ExectorFactory.create_executor("summary")
    executor.dispatch()