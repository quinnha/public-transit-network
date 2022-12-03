from station import Station
from itertools import permutations
from island import Island
from sys import maxsize


class GraphImplementation:
    # CSV for this implementation
    # skips "ghost station", so adding manually
    # for easy indexing
    def __init__(self):
        self.num_stations = 0  # int
        self.num_connections = 0  # int
        self.avg_degree = 0  # int
        self.stations = [
            Station("Indexer", -1, 0, -1, -1),
            Station("Ghost Station", 189, -1, -1, -1),
        ]  # list of stations
        self.a_list = {}  # key:value = int:[connections]
        self.zones = {}  # dic of zone float(id):zone object

    # Factory design pattern to hold all metrics
    def get_metrics(self):
        out = ""
        for key in self.metrics.keys():
            out += key + " - " + self.metrics[key].getMetric() + ", "

        return out[0:-1]

    # Adding a station changes some of the member variables
    def add_station(self, station):
        self.num_stations += 1
        self.num_connections += len(station.connections)
        self.stations.append(station)
        self.stations.sort()
        self.a_list[station.id] = station.connections
        self.average_degree()
        pass

    # Calculating Average Degree
    def average_degree(self):
        total = 0
        for station in self.stations:
            total += len(station.connections)
        self.avg_degree = total / self.num_stations

    # Display function with all relevant information
    def display(self):
        print("Number of stations: ", self.num_stations)
        print("Number of connections: ", self.num_connections)
        print("Number of zones: ", len(self.zones))
        print("Average degree:", self.avg_degree)
        print("\nListing stations:\n")
        for station in self.stations:
            station.display()

        print("\nPrinting Adjacency List\n")
        for key in self.a_list.keys():
            out = str(key) + ": ["
            for i in range(len(self.a_list.get(key))):
                out += (str(self.a_list.get(key)[i].to)) + " "
            out = out[:-1]
            out += "] "
            print(out)

    # Dijkstra's algorithm
    def dijkstra(self, start_station, end_station, t="dijkstra"):
        # Dijkstra's is a special case of a_star, so pass the value
        # to recognize that it's dijkstra's in heuristic function
        return self.a_star(start_station, end_station, t)

    # defining logic for a_star and dijkstra's
    def heuristic(self, current_station, end_station, t):
        # No heuristic for dijkstra's
        if t == "dijkstra":
            return 0
        # Manhattan distance for a_star
        else:
            return (current_station.longitude - end_station.longitude) ** 2 + (
                current_station.latitude - end_station.latitude
            ) ** 2

    # Shortest path algorithm
    def a_star(self, start_station, end_station, t):
        # open_list is a list of nodes which
        # have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected

        if start_station == end_station:
            return [start_station], 0

        open_list = set([start_station])
        closed_list = set([])

        reconst_path = []

        # keeping track of distance of each node
        # to the start as a key:value for easy referencing
        dist_start = {}

        dist_start[start_station] = 0

        # parents = adjacency map of each node
        parents = {}
        parents[start_station] = start_station

        while len(open_list) > 0:
            n = 1

            # Finding node with lowest cost (f = g + h)
            for station in open_list:
                if n == 1 or dist_start[station] + self.heuristic(
                    station, end_station, t
                ) < dist_start[n] + self.heuristic(n, end_station, t):
                    n = station
            if n == 1:
                return -1

            # If we hit the target station,
            # then we have to reconstruct the parth to return
            if n == end_station:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_station)
                reconst_path.reverse()

                # Get weight between every station
                weight = 0
                r_point = 1
                for station in reconst_path:
                    for i in range(len(station.connections)):
                        connection = station.connections[i].to
                        if connection == reconst_path[r_point].id:
                            weight += station.connections[i].weight
                            break
                    r_point += 1
                    if r_point == len(reconst_path):
                        break

                return reconst_path, weight

            # Go through all the neighbours, if node hasnt been marked,
            # mark it in open_list, and n becomes its parent
            for connection in n.connections:
                neighbour = self.stations[connection.to]

                # Otherwise, check if it's quicker to first
                # visit n, then m and if it is,
                # update parent data and g data
                # and if the node was in the closed_list,
                # move it to open_list
                if neighbour not in open_list and neighbour not in closed_list:
                    open_list.add(neighbour)
                    parents[neighbour] = n
                    dist_start[neighbour] = dist_start[n] + connection.weight

                else:
                    dist_neighbour = dist_start[neighbour]
                    dist_n = dist_start[n]
                    if dist_neighbour > dist_n + connection.weight:
                        dist_neighbour = dist_n + connection.weight
                        parents[neighbour] = n

                        if neighbour in closed_list:
                            closed_list.remove(neighbour)
                            open_list.add(neighbour)

            # Remove n from the open_list,
            # and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

    def subwayPatrol(self, stations, start_station):

        # travelling salesman, get shortest path
        # that visits all stations and returns to
        # start station with djikstra

        # base case
        if len(stations) == 1:
            return [start_station], 0

        # store all stations apart from sourec vertex
        vertex = []
        for i in range(len(stations)):
            if stations[i] != start_station:
                vertex.append(stations[i])
        min_path_list = []
        min_pathweight = maxsize
        next_permutation = permutations(vertex)
        for i in next_permutation:
            current_pathweight = 0
            # compute current path weight
            k = start_station
            for j in i:
                _, weight = self.a_star(k, j, "dijkstra")
                if weight == -1:
                    continue
                current_pathweight += weight
                k = j
            _, weight = self.a_star(k, start_station, "dijkstra")
            if weight == -1:
                continue

            current_pathweight += weight

            # update minimum
            if current_pathweight < min_pathweight:
                min_pathweight = current_pathweight
                min_path_list = i
        return_path = [start_station]
        return_path.extend(min_path_list)
        # because we are going back and forth, need to divide by 2
        min_pathweight = min_pathweight / 2
        # dumb formatting for flake >:(
        m_p_l = min_path_list[-1]
        s_s = start_station
        path_back, weight_back = self.dijkstra(m_p_l, s_s)
        min_pathweight += weight_back
        return_path.extend(path_back[1:])
        return return_path, int(min_pathweight)

    def createIslands(self):
        # Get all islands for each
        # zone, and store them in zone.islands
        for key in self.zones.keys():
            i = 0
            zone = self.zones[key]
            visited = {}
            cc = []

            for station in zone.stations:
                visited[station] = False
            # Recursively calling DFS
            # to find all connected components
            for station in zone.stations:
                if not visited[station]:
                    temp = []
                    cc.append(
                        Island(
                            i + float(zone.id),
                            float(zone.id),
                            self.dfs(temp, station, visited),
                        )
                    )
                    i += 0.01
            zone.islands = cc

    # DFS Implementation, if a station
    # is visited, it is added to the island
    def dfs(self, temp, station, visited):
        visited[station] = True
        temp.append(station)
        for connection in station.connections:
            neighbour = self.stations[connection.to]
            if neighbour not in visited.keys():
                continue
            if not visited[neighbour]:
                temp = self.dfs(temp, neighbour, visited)
        return temp

    # Checking to see how islands are connected to each other,
    # and how the zones are connected to each other
    def connectIslands(self):
        # In zone connection dic, track all islands conencted to eachother
        for key in self.zones.keys():
            zone = self.zones[key]
            for island in zone.islands:
                for connection in island.stations[0].connections:
                    neighbour = self.stations[connection.to]
                    try:
                        if float(neighbour.zone) == float(island.zone):
                            continue
                        # dumb formatting for flake >:(
                        z = float(neighbour.zone)
                        if z not in zone.connections.keys():
                            zone.connections[float(neighbour.zone)] = []
                        zone.connections[float(neighbour.zone)].append(island)
                    except ValueError:
                        continue
                    break

    # Parsing Zone connections for graph
    def displayZoneConnections(self):
        out = ""
        for key in self.zones.keys():
            for key_ in self.zones[key].connections.keys():
                out += (str(self.zones[key_].id) + ", ")
            this_zone = str(self.zones[key].id)
            print("Zone: " + this_zone + " connects to zone: " + out[:-2])
            out = ""
