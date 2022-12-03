# A Zone is a subset of stations in a graph


class Zone:

    def __init__(self, id):
        self.id = id
        self.stations = []
        self.connections = {}
        self.islands = []

    def display(self):
        print("Zone: " + str(self.id))
        print("Stations: ")
        out = ""
        for station in self.stations:
            out += (station.name + ", ")
        print(out[:-2])
        out = ""
