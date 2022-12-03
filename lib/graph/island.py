# A Island is a subset of stations in a zone
class Island:

    def __init__(self, id, zone, stations):
        self.id = id
        self.zone = zone
        self.stations = stations

    def display(self):
        print("Island: " + str(self.id))
        print("Zone: " + str(self.zone))
        print("Stations: ")
        out = ""
        for station in self.stations:
            out += (station.name + ", ")
        print(out[:-2])
        out = ""
