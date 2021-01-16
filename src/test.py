import unittest
import time
from GraphAlgo import GraphAlgo
import networkx
import json



class Tests(unittest.TestCase):

    def test_networkx_load_json(self):
        print()
        G_10_80_0 = '../test/G_10_80_0.json'
        G_100_800_0 = '../test/G_100_800_0.json'
        G_1000_8000_0 = '../test/G_1000_8000_0.json'
        G_10000_80000_0 = '../test/G_10000_80000_0.json'
        G_20000_160000_0 = '../test/G_10000_80000_0.json'
        G_30000_240000_0 = '../test/G_30000_240000_0.json'

        G_10_80_1 = '../test/G_10_80_1.json'
        G_100_800_1 = '../test/G_100_800_1.json'
        G_1000_8000_1 = '../test/G_1000_8000_1.json'
        G_10000_80000_1 = '../test/G_10000_80000_1.json'
        G_20000_160000_1 = '../test/G_10000_80000_1.json'
        G_30000_240000_1 = '../test/G_30000_240000_1.json'

        G_10_80_2 = '../test/G_10_80_2.json'
        G_100_800_2 = '../test/G_100_800_2.json'
        G_1000_8000_2 = '../test/G_1000_8000_2.json'
        G_10000_80000_2 = '../test/G_10000_80000_2.json'
        G_20000_160000_2 = '../test/G_10000_80000_2.json'
        G_30000_240000_2 = '../test/G_30000_240000_2.json'

        algo = GraphAlgo()
        file_list = [G_10_80_0, G_100_800_0, G_1000_8000_0, G_10000_80000_0, G_20000_160000_0,G_30000_240000_0,
                     G_10_80_1, G_100_800_1, G_1000_8000_1, G_10000_80000_1, G_20000_160000_1, G_30000_240000_1,
                     G_10_80_2, G_100_800_2, G_1000_8000_2, G_10000_80000_2, G_20000_160000_2, G_30000_240000_2]

        for file_name in file_list:

            #   load graph from networkx
            networkx_graph = networkx.DiGraph()

             # by networkx documentation
            file = open(file_name)
            data = json.load(file)

            nodes = []
            edges = []

            for node in data['Nodes']:
                nodes.append(node['id'])

            for edge in data['Edges']:
                edges.append((edge['src'], edge['dest'], edge['w']))

            networkx_graph.add_nodes_from(nodes)
            networkx_graph.add_weighted_edges_from(edges)

            start = time.perf_counter()
            # execute logic

            networkx.shortest_path(0, 10)

            print("time took to networkx shortestpath {}: {}".format(file_name, time.perf_counter()-start))

    def test_networkx_load_json(self):
        print()
        G_10_80_0 = '../test/G_10_80_0.json'
        G_100_800_0 = '../test/G_100_800_0.json'
        G_1000_8000_0 = '../test/G_1000_8000_0.json'
        G_10000_80000_0 = '../test/G_10000_80000_0.json'
        G_20000_160000_0 = '../test/G_10000_80000_0.json'
        G_30000_240000_0 = '../test/G_30000_240000_0.json'

        G_10_80_1 = '../test/G_10_80_1.json'
        G_100_800_1 = '../test/G_100_800_1.json'
        G_1000_8000_1 = '../test/G_1000_8000_1.json'
        G_10000_80000_1 = '../test/G_10000_80000_1.json'
        G_20000_160000_1 = '../test/G_10000_80000_1.json'
        G_30000_240000_1 = '../test/G_30000_240000_1.json'

        G_10_80_2 = '../test/G_10_80_2.json'
        G_100_800_2 = '../test/G_100_800_2.json'
        G_1000_8000_2 = '../test/G_1000_8000_2.json'
        G_10000_80000_2 = '../test/G_10000_80000_2.json'
        G_20000_160000_2 = '../test/G_10000_80000_2.json'
        G_30000_240000_2 = '../test/G_30000_240000_2.json'

        algo = GraphAlgo()

        file_list = [G_10_80_0, G_100_800_0, G_1000_8000_0, G_10000_80000_0, G_20000_160000_0,G_30000_240000_0,
                     G_10_80_1, G_100_800_1, G_1000_8000_1, G_10000_80000_1, G_20000_160000_1, G_30000_240000_1,
                     G_10_80_2, G_100_800_2, G_1000_8000_2, G_10000_80000_2, G_20000_160000_2, G_30000_240000_2]

        start1 = time.time()
        for file_name in file_list:

            start = time.perf_counter()
            # execute logic

            #   load graph from networkx
            networkx_graph = networkx.DiGraph()

             # by networkx documentation
            file = open(file_name)
            data = json.load(file)

            nodes = []
            edges = []

            for node in data['Nodes']:
                nodes.append(node['id'])

            for edge in data['Edges']:
                edges.append((edge['src'], edge['dest'], edge['w']))

            networkx_graph.add_nodes_from(nodes)
            networkx_graph.add_weighted_edges_from(edges)


            print("time took to networkx load {}: {}".format(file_name, time.perf_counter()-start))
            file.close()
        print("time took to load all fiels: {}".format( time.time()-start1))

    def test_connected_components(self):
        print()
        G_10_80_0 = '../test/G_10_80_0.json'
        G_100_800_0 = '../test/G_100_800_0.json'
        G_1000_8000_0 = '../test/G_1000_8000_0.json'
        G_10000_80000_0 = '../test/G_10000_80000_0.json'
        G_20000_160000_0 = '../test/G_10000_80000_0.json'
        G_30000_240000_0 = '../test/G_30000_240000_0.json'

        G_10_80_1 = '../test/G_10_80_1.json'
        G_100_800_1 = '../test/G_100_800_1.json'
        G_1000_8000_1 = '../test/G_1000_8000_1.json'
        G_10000_80000_1 = '../test/G_10000_80000_1.json'
        G_20000_160000_1 = '../test/G_10000_80000_1.json'
        G_30000_240000_1 = '../test/G_30000_240000_1.json'

        G_10_80_2 = '../test/G_10_80_2.json'
        G_100_800_2 = '../test/G_100_800_2.json'
        G_1000_8000_2 = '../test/G_1000_8000_2.json'
        G_10000_80000_2 = '../test/G_10000_80000_2.json'
        G_20000_160000_2 = '../test/G_10000_80000_2.json'
        G_30000_240000_2 = '../test/G_30000_240000_2.json'

        algo = GraphAlgo()

        file_list = [G_10_80_0, G_100_800_0, G_1000_8000_0, G_10000_80000_0, G_20000_160000_0,G_30000_240000_0,
                     G_10_80_1, G_100_800_1, G_1000_8000_1, G_10000_80000_1, G_20000_160000_1, G_30000_240000_1,
                     G_10_80_2, G_100_800_2, G_1000_8000_2, G_10000_80000_2, G_20000_160000_2, G_30000_240000_2]

        for file_name in file_list:
            algo.load_from_json(file_name)

            start = time.perf_counter()
            # execute logic

            algo.connected_components()

            print("time took to connected component {}: {}".format(file_name, time.perf_counter()-start))

    def test_shortest_path_0_10(self):
        print()
        G_10_80_0 = '../test/G_10_80_0.json'
        G_100_800_0 = '../test/G_100_800_0.json'
        G_1000_8000_0 = '../test/G_1000_8000_0.json'
        G_10000_80000_0 = '../test/G_10000_80000_0.json'
        G_20000_160000_0 = '../test/G_10000_80000_0.json'
        G_30000_240000_0 = '../test/G_30000_240000_0.json'

        G_10_80_1 = '../test/G_10_80_1.json'
        G_100_800_1 = '../test/G_100_800_1.json'
        G_1000_8000_1 = '../test/G_1000_8000_1.json'
        G_10000_80000_1 = '../test/G_10000_80000_1.json'
        G_20000_160000_1 = '../test/G_10000_80000_1.json'
        G_30000_240000_1 = '../test/G_30000_240000_1.json'

        G_10_80_2 = '../test/G_10_80_2.json'
        G_100_800_2 = '../test/G_100_800_2.json'
        G_1000_8000_2 = '../test/G_1000_8000_2.json'
        G_10000_80000_2 = '../test/G_10000_80000_2.json'
        G_20000_160000_2 = '../test/G_10000_80000_2.json'
        G_30000_240000_2 = '../test/G_30000_240000_2.json'

        algo = GraphAlgo()

        file_list = [G_10_80_0, G_100_800_0, G_1000_8000_0, G_10000_80000_0, G_20000_160000_0,G_30000_240000_0,
                     G_10_80_1, G_100_800_1, G_1000_8000_1, G_10000_80000_1, G_20000_160000_1, G_30000_240000_1,
                     G_10_80_2, G_100_800_2, G_1000_8000_2, G_10000_80000_2, G_20000_160000_2, G_30000_240000_2]

        for file_name in file_list:
            algo.load_from_json(file_name)

            start = time.perf_counter()
            # execute logic

            algo.shortest_path(0, 10)

            print("time took to shortest_path in from 0-10 {}: {}".format(file_name, time.perf_counter()-start))

    # test run time - load json
    def test_load_from_json(self):
        print()
        G_10_80_0 = '../test/G_10_80_0.json'
        G_100_800_0 = '../test/G_100_800_0.json'
        G_1000_8000_0 = '../test/G_1000_8000_0.json'
        G_10000_80000_0 = '../test/G_10000_80000_0.json'
        G_20000_160000_0 = '../test/G_10000_80000_0.json'
        G_30000_240000_0 = '../test/G_30000_240000_0.json'

        G_10_80_1 = '../test/G_10_80_1.json'
        G_100_800_1 = '../test/G_100_800_1.json'
        G_1000_8000_1 = '../test/G_1000_8000_1.json'
        G_10000_80000_1 = '../test/G_10000_80000_1.json'
        G_20000_160000_1 = '../test/G_10000_80000_1.json'
        G_30000_240000_1 = '../test/G_30000_240000_1.json'

        G_10_80_2 = '../test/G_10_80_2.json'
        G_100_800_2 = '../test/G_100_800_2.json'
        G_1000_8000_2 = '../test/G_1000_8000_2.json'
        G_10000_80000_2 = '../test/G_10000_80000_2.json'
        G_20000_160000_2 = '../test/G_10000_80000_2.json'
        G_30000_240000_2 = '../test/G_30000_240000_2.json'

        algo = GraphAlgo()

        file_list = [G_10_80_0, G_100_800_0, G_1000_8000_0, G_10000_80000_0, G_20000_160000_0,G_30000_240000_0,
                     G_10_80_1, G_100_800_1, G_1000_8000_1, G_10000_80000_1, G_20000_160000_1, G_30000_240000_1,
                     G_10_80_2, G_100_800_2, G_1000_8000_2, G_10000_80000_2, G_20000_160000_2, G_30000_240000_2]

        for file_name in file_list:

            start = time.perf_counter()

            # execute logic

            algo.load_from_json(file_name)

            print("time took to load {}: {}".format(file_name, time.perf_counter()-start))


if __name__ == '__main__':
    unittest.main()