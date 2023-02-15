from multiprocessing import Process, Queue, cpu_count
import time

from utils.logger.logger import Logger


class Consumer(Process):
    @property
    def queue(self):
        return self.__queue

    def __init__(self, queue: Queue):
        Process.__init__(self)
        self.__queue = queue

    def run(self):
        self.__logger = Logger()
        while not(self.__queue.empty()):
            self.__logger.info(self.__class__, f"get : {self.__queue.get()}")
            time.sleep(2)


class Provider(Process):
    def __init__(self, queue: Queue):
        Process.__init__(self)
        self.__queue = queue

    def run(self):
        self.__logger = Logger()
        for i in range(10):
            self.__queue.put(i)
            time.sleep(1)
            self.__logger.info(self.__class__, f"put : {i}")


class SummaryExecutor():
    def __init__(self):
        self.__logger = Logger()
        self.__logger.info(self.__class__)

    def dispatch(self):
        queue = Queue()

        providers = [
            Provider(queue) for _ in range(1)            
        ]

        consumers = [
            Consumer(queue) for _ in range(4)
        ]
        processes = []        
        for p in providers:
            p.start()
            processes.append(p)

        for c in consumers:
            c.start()
            processes.append(c)

        for p in processes:
            p.join()

        return None