from metric import metric


class NodeDistribution(metric):

    def __init__(self, item):
        out_dict = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0

        }
        # count the degree of each node and store into a dictionary
        for station in item.stations:
            if len(station.connections) != 0:
                out_dict[len(station.connections)] += 1
        self.dic = out_dict

    def getMetric(self):
        return "n/a"
