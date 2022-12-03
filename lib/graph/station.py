# Station class with relevant information


class Station:
    def __init__(self, name, id, zone, longitude, latitude):
        self.name = name  # string
        self.id = id  # int
        self.zone = zone  # int
        self.longitude = longitude
        self.latitude = latitude
        self.connections = []  # list of connection objects
        self.lines = []  # list of line objects

    def __lt__(self, other):
        return self.id < other.id

    def display(self):
        out = "Station: " + self.name + \
            " (id: " + str(self.id) + ") Zone: " + \
            str(self.zone) + " Connections: ["
        for connection in self.connections:
            out += (str(connection.to) + " ")
        out = out[:-1]
        out += "]"
        print(out)
