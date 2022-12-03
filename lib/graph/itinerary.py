# The Itenerary class is used to store
# the path and time of a journey across stations


class Itinerary:
    def __init__(self, graph, start_station, end_station, method="a_star"):
        self.graph = graph
        self.start_station = start_station
        self.end_station = end_station
        self.itinerary = []
        self.time = 0
        # User can determine what algorithm
        # they want to use to find the shortest path
        self.method = method

    def travel(self, method):
        self.itinerary, self.time = self.graph.a_star(
            self.start_station, self.end_station, method
        )

    def display(self):
        for station in self.itinerary:
            station.display()
        print("Total time: " + str(self.time))
