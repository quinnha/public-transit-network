import csv
from graph_implementation import GraphImplementation
from station import Station
from connections import Connection
from zone import Zone
import os

# Building the graph


class GraphBuilderImplementation:

    # Using the Contructor to initialize the graph
    def __init__(self):
        station_list_str = []
        station_list = []
        station_dic = {}
        zones = []

        # Reading CSV to get station information,
        # and load it into a dictionary to put in graph
        station_path = os.path.dirname(__file__)
        station_path = os.path.join(
            station_path, "../../_dataset/london.stations.csv"
            )
        with open(station_path, newline="") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
            for row in spamreader:
                station_list_str.append(
                    " ".join(row).replace('"', "").split(",")
                    )

        # Remove header for CSV list
        station_list_str = station_list_str[1:]

        # Loading into dictionary of stations, id:station
        for station_info in station_list_str:
            id = station_info[0]
            latitude = station_info[1]
            longitude = station_info[2]
            name = station_info[3]
            zone = station_info[5]
            station_list.append(
                Station(name, int(id), zone, float(longitude), float(latitude))
            )
            # store in dic for O(1) lookup
            station_dic[int(id)] = station_list[-1]
            zones.append(zone)

        # Create a list of Zone objects for the Graph
        zone_dic = {}
        zones = list(set(zones))

        # Some inputs are strings, remove them
        for zone in sorted(zones):
            try:
                zone_dic[float(zone)] = Zone(zone)
            except ValueError:
                continue

        # Load Zone objects into Station objects
        for station in station_list:
            try:
                zone_dic[float(station.zone)].stations.append(station)
            except ValueError:
                continue

        # Creating Connection objects (connections between stations)

        connection_list = []

        # Reading CSV to get Connection object,
        # and loading into Station Dictionary
        station_path = os.path.dirname(__file__)
        station_path = os.path.join(
            station_path, "../../_dataset/london.connections.csv"
            )
        with open(station_path, newline="") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
            for row in spamreader:
                connection_list.append(
                    " ".join(row).replace('"', "").split(",")
                    )

        connection_list = connection_list[1:]

        for connections in connection_list:
            s1 = int(connections[0])
            s2 = int(connections[1])
            line = int(connections[2])
            weight = int(connections[3])
            station_dic.get(s1).connections.append(
                Connection(s1, s2, line, weight)
                )
            station_dic.get(s2).connections.append(
                Connection(s2, s1, line, weight)
                )

        # Loading all data into Graph object

        map_graph = GraphImplementation()

        for key in station_dic.keys():
            map_graph.add_station(station_dic.get(key))

        # Undirected graph, all connections are
        # bidirectional, so have to divide by 2

        map_graph.num_connections = map_graph.num_connections // 2

        map_graph.zones = zone_dic

        self.graph = map_graph
