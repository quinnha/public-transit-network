from itinerary import Itinerary
from graph_builder_implementation import GraphBuilderImplementation
import pyperf
import random


def bench():
    # Benchmarking execution time of Dijkstra and A* algorithms
    random.seed(827359046)

    algorithms = ["dijkstra", "a_star"]
    builder = GraphBuilderImplementation()
    bench_map = builder.graph
    station_1_id = random.randrange(1, 303)
    station_2_id = random.randrange(1, 303)
    station_1 = bench_map.stations[station_1_id]
    station_2 = bench_map.stations[station_2_id]

    itinerary = Itinerary(bench_map, station_1, station_2, "")

    do_bench(itinerary, algorithms)


def do_bench(itinerary, algorithms):

    runner = pyperf.Runner()

    for algorithm in algorithms:
        runner.bench_func(algorithm, itinerary.travel, algorithm)


if __name__ == "__main__":
    bench()
