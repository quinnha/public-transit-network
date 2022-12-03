from metric import metric


class NumConnections(metric):

    def __init__(self, item):

        count = 0
        for station in item.stations:
            count += len(station.connections)

        self.num_connections = count/2

    def getMetric(self):
        return str(self.num_connections)
