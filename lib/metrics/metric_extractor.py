from abc import ABC, abstractmethod

# factory


class MetricExtractor(ABC):

    @abstractmethod
    def __init__(self, item):
        pass

    @abstractmethod
    def set_metrics(self):
        pass

    @abstractmethod
    def display(self):
        pass
