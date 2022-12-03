from abc import ABC, abstractmethod


class metric(ABC):

    @abstractmethod
    def __init__(self, graph):
        pass

    @abstractmethod
    def getMetric(self):
        pass
