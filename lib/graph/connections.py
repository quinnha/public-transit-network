# Connection class between two Stations, and between two Zones
class Connection():
    def __init__(self, origin, to, line, weight):
        self.origin = origin  # origin station being refered to
        self.to = to  # connection to
        self.weight = weight  # weight of the connection
        self.line = line  # what line it belongs to

    # Debug print output
    def display(self):
        print("Origin: ", self.origin, " Destination: ", self.to,
              " Time: ", self.weight, " Line: ", self.line)
