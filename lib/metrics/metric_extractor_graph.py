from metric_extractor import MetricExtractor
from average_degree import AverageDegree
from num_stations import NumStations
from num_connections import NumConnections
from node_distribution import NodeDistribution
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../graph'))


# factory

class MetricExtractorGraph(MetricExtractor):

    def __init__(self, graph):
        self.graph = graph
        self.metrics = {}

    def set_metrics(self):
        self.metrics = {
            "num_stations": NumStations(self.graph),
            "num_connections": NumConnections(self.graph),
            "average_degree": AverageDegree(self.graph),
            "degree_distribution": NodeDistribution(self.graph)
        }

    def display(self):
        out = ""
        for key in self.metrics.keys():
            out += (key + " - " + self.metrics[key].getMetric() + "\n")
        print(out[:-1])  # remove last comma
