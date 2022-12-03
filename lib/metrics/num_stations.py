from metric import metric


class NumStations(metric):

    def __init__(self, item):
        self.stations = len(item.stations)

    def getMetric(self):
        return str(self.stations)
