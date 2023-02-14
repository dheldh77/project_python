from abc import ABCMeta, abstractclassmethod
from summary.summary_executor import SummaryExecutor


class ExectorFactory:
    @classmethod
    def create_executor(cls, executor: str):
        if executor.lower() == "summary":
            return SummaryExecutor()
        if executor.lower() == "analysis":
            return None


class Executor(metaclass=ABCMeta):
    @abstractclassmethod
    def dispatch(self):
        pass