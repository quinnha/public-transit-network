import sys
import os

# From Lab 1 TA, ignore flake8 errors
sys.path.append(os.path.join(os.path.dirname(__file__), "../graph"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../metrics"))
from metric_extractor_graph import MetricExtractorGraph  # noqa: E402
from graph_builder_implementation import GraphBuilderImplementation  # noqa

builder = GraphBuilderImplementation()
graph = builder.graph


def test_impl():
    # Testing graph builder
    assert graph.num_stations == 302
    assert graph.num_connections == 406

    # Testing Dijkstra
    test_dijkstra()

    # Testing a_star
    test_a_star()

    # Testing metric extractor
    test_metric_extractor()

    # Testing subwayPatrol
    test_subwayPatrol()

    print("All tests passed")


def test_dijkstra():

    # Testing general case
    return_stations = [
        graph.stations[11],
        graph.stations[83],
        graph.stations[193],
        graph.stations[218],
        graph.stations[283],
        graph.stations[147],
        graph.stations[150],
        graph.stations[227]
    ]

    path, weight = graph.dijkstra(graph.stations[11], graph.stations[227])

    for i in range(len(path)):
        # print(path[i].id)
        assert path[i] == return_stations[i]
    assert weight == 14

    # Testing start and end are the same
    return_stations = [graph.stations[11]]
    path, weight = graph.dijkstra(graph.stations[11], graph.stations[11])

    for i in range(len(return_stations)):
        assert path[i] == return_stations[i]
    assert weight == 0


def test_a_star():
    # Testing general case
    return_stations = [
        graph.stations[11],
        graph.stations[83],
        graph.stations[193],
        graph.stations[218],
        graph.stations[283],
        graph.stations[147],
        graph.stations[150],
        graph.stations[227]
    ]

    path, weight = graph.a_star(
        graph.stations[11], graph.stations[227], "a_star"
        )

    for i in range(len(return_stations)):
        assert path[i] == return_stations[i]
    assert weight == 14

    # Testing start and end are the same
    return_stations = [graph.stations[11]]
    path, weight = graph.dijkstra(
        graph.stations[11], graph.stations[11]
        )

    for i in range(len(return_stations)):
        assert path[i] == return_stations[i]
    assert weight == 0


def test_metric_extractor():
    extractor = MetricExtractorGraph(graph)
    extractor.set_metrics()

    # Getting the metrics from the extractor
    assert extractor.metrics["num_stations"].getMetric() == "304"
    assert extractor.metrics["num_connections"].getMetric() == "406.0"
    x = "2.6710526315789473"
    assert extractor.metrics["average_degree"].getMetric() == x


def test_subwayPatrol():
    # Testing general case
    start_station = graph.stations[11]
    stations = [
        graph.stations[11],
        graph.stations[83],
        graph.stations[193],
        graph.stations[218],
        graph.stations[283]
    ]
    test_stations = [
        graph.stations[11],
        graph.stations[83],
        graph.stations[193],
        graph.stations[218],
        graph.stations[283],
        graph.stations[218],
        graph.stations[193],
        graph.stations[83],
        graph.stations[11]
    ]
    path, weight = graph.subwayPatrol(stations, start_station)

    for i in range(len(path)):
        assert path[i] == test_stations[i]
    assert weight == 18

    # Testing length 1 patrol
    start_station = graph.stations[11]
    stations = [graph.stations[11]]
    path, weight = graph.subwayPatrol(stations, start_station)
    assert path[0] == start_station
    assert weight == 0


if __name__ == "__main__":
    """We read the input data from the standard input,
    and print the result to the standard output"""
    test_impl()
