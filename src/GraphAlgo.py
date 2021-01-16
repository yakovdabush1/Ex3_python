from typing import List
from src import GraphInterface
import json
import sys
from src.DiGraph import DiGraph
import heapq
import matplotlib.pyplot as plt


class GraphAlgo:

    def __init__(self, graph=None):
        self.graph = graph

        # two "hashmaps" for djikstra
        self.distance = {}
        self.parents = {}

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

        graph = DiGraph()

        try:

            # open file with 'r'=read mode
            file = open(file_name, 'r')

            json_data = json.load(file)

            for node_json in json_data['Nodes']:

                try:
                    # try to read pos
                    s = node_json['pos']
                    split_s = s.split(",")

                    x, y, z = float(split_s[0]), float(split_s[1]), float(split_s[2])
                    graph.add_node(node_json['id'], (x, y, z))

                except:
                    # read without pos
                    graph.add_node(node_json['id'])

            for edge_json in json_data["Edges"]:
                graph.add_edge(edge_json['src'], edge_json['dest'], edge_json['w'])

            self.graph = graph
            file.close()
            return True

        except OSError as err:
            print("error: {}".format(err))
            return False

        except:
            print("unexpected error ", sys.exc_info()[0])
            return False

    def save_to_json(self, file_name: str) -> bool:  # {
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """
        try:
            # new dict to represent json
            json_dict = {"Nodes": [], "Edges": []}

            node_list = self.graph.get_all_v()

            for node_key in node_list:
                node = node_list[node_key]

                # convert pos from tuple to string
                if node.pos is None:
                    x, y, z = 0.0, 0.0, 0.0

                else:
                    x, y, z = node.pos

                pos_string = "{},{},{}".format(x, y, z)

                json_dict["Nodes"].append({
                    "id": node_key,
                    "pos": pos_string
                })

                for out in node_list[node_key].out_neighbors:

                    json_dict["Edges"].append({
                        "src": node_key,
                        "dest": out,
                        "w": node_list[node_key].out_neighbors[out]
                    })

            # open file with 'w'=write mode
            file = open(file_name, 'w')
            # use json.dump to write data to file
            json.dump(json_dict, file)
            file.close()
            return True

        except OSError as err:
            print("error: {}".format(err))
            return False

        except:
            print("unexpected error ", sys.exc_info()[0])
            return False

    def djikstra(self, src_node):
        """
        algorithm for djkistra using priority queue
        :param src_node:
        :return:
        """
        # for key i in node dict
        for i in self.graph.get_all_v():
            self.distance[i] = float('inf')

        self.distance = {i: float('inf') for i in self.graph.get_all_v()}
        self.parents = {i: None for i in self.graph.get_all_v()}

        # insert into list tuple -> (priority, node_key)
        # the
        priority_queue = [(0.0, src_node)]
        self.distance[src_node] = 0.0

        while priority_queue:

            min_distance, node_key = heapq.heappop(priority_queue)

            # for all neighbors of node
            out_edges = self.graph.all_out_edges_of_node(node_key)
            for ni_key in out_edges:

                alt = self.distance[node_key] + out_edges[ni_key]

                if alt < self.distance[ni_key]:
                    self.distance[ni_key] = alt
                    self.parents[ni_key] = node_key

                    heapq.heappush(priority_queue, (alt, ni_key))

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        node_list = self.graph.get_all_v()
        if id1 not in node_list or id2 not in node_list:
            return float('inf'), []

        # fill distance and parent dict
        self.djikstra(id1)

        shortest_dist = self.distance[id2]

        index_runner = id2
        shortest_path = [index_runner]

        while index_runner is not None:
            shortest_path.append(self.parents[index_runner])
            index_runner = self.parents[index_runner]

            if index_runner == id1:
                # shortest_path[::-1] -> reverse traverse
                return shortest_dist, shortest_path[::-1]

            if index_runner is None:
                return shortest_dist, []

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """

        """
        dfs(src)
        transpose_graph
        dfs(src)
        """
        if id1 in self.graph.get_all_v():

            components = self.connected_components()
            for component in components:
                if id1 in component:
                    return component

        return []

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        # part 1 -> dfs with stack
        stack = []
        visited = [False] * self.graph.v_size()

        for node_key in self.graph.get_all_v():


            if node_key in visited:
                # node and all its branches have been visited
                return stack, visited

            # if not visited[node_key]:
            self.dfs_stack(node_key, visited, stack)

        # part 2 -> transpose graph
        transpose_graph = DiGraph()
        for node_key in self.graph.get_all_v():
            transpose_graph.add_node(node_key)

        for node_key in self.graph.get_all_v():
            outs = self.graph.all_out_edges_of_node(node_key)
            for dest_key in outs:
                transpose_graph.add_edge(dest_key, node_key, outs[dest_key])

        # part 3 -> dfs from stack
        visited = [False] * self.graph.v_size()
        components = []

        while stack:
            key = stack.pop()
            if not visited[key]:
                c = self.dfs_scc(key, visited, [], transpose_graph)
                components.append(c)

        return components

    def dfs_stack(self, current_node, visited, stack):

        visited[current_node] = True

        for dest_key in self.graph.all_out_edges_of_node(current_node):
            if not visited[dest_key]:
                self.dfs_stack(dest_key, visited, stack)

        stack.append(current_node)

    def dfs_scc(self, current_node, visited, scc_list, transpoe_graph):
        visited[current_node] = True

        scc_list.append(current_node)

        for dest_key in transpoe_graph.all_out_edges_of_node(current_node):
            if not visited[dest_key]:
                self.dfs_scc(dest_key, visited, scc_list, transpoe_graph)

        return scc_list

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """

        """
        import matplotlib.pyplot as plt
        matplotlib -> https://matplotlib.org/ 
        """

        # for n in self.graph.get_all_v():
        #
        #     node = self.graph.nodes[n]
        #
        #     node.update_position(self.graph.v_size())

        ax = plt.axes()

        pos_x = []
        pos_y = []

        for n in self.graph.get_all_v():

            node = self.graph.nodes[n]
            if node.pos is None: node.update_position(self.graph.v_size())
            x, y, z = node.pos

            pos_x.append(x)
            pos_y.append(y)

            for dest_key in self.graph.all_out_edges_of_node(n):

                dest_node = self.graph.nodes[dest_key]
                if dest_node.pos is None: dest_node.update_position(self.graph.v_size())
                dest_x, dest_y, dest_z = dest_node.pos

                # (x,y) -> (x+dx, y+dy)
                ax.quiver(x, y, dest_x-x, dest_y-y, angles='xy', scale_units='xy', scale=1)



        plt.plot(pos_x, pos_y, 'ro')
        plt.show()