from metric import metric


class AverageDegree(metric):

    def __init__(self, item):
        total = 0
        for station in item.stations:
            total += len(station.connections)
        self.avg_degree = total/len(item.stations)

    def getMetric(self):
        return str(self.avg_degree)
