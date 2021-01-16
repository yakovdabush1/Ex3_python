from src.Node_Data import Node_Data


class DiGraph:

    def __init__(self):
        self.nodes = {}

        self.mc = 0
        self.edge_size = 0
        self.node_size = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.node_size

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edge_size

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using apair  (key, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """

        if id1 in self.nodes:
            return self.nodes[id1].in_neighbors

        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """

        if id1 in self.nodes:
            return self.nodes[id1].out_neighbors

        return {}

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """

        if id1 is not id2 and id1 in self.nodes and id2 in self.nodes:

            node1 = self.nodes[id1]
            node2 = self.nodes[id2]

            if weight > 0 and id2 not in node1.out_neighbors and id1 not in node2.in_neighbors:

                node1.out_neighbors[id2] = weight
                node2.in_neighbors[id1] = weight

                self.edge_size = self.edge_size + 1
                self.mc += 1

                return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """

        if node_id not in self.nodes:

            self.nodes[node_id] = Node_Data(node_id, pos)
            self.node_size += 1

            return True

        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """

        if node_id not in self.nodes:
            return False

        node = self.nodes[node_id]

        outs = node.out_neighbors
        ins = node.in_neighbors

        for n in outs:
            del self.nodes[n].in_neighbors[node_id]
            self.edge_size -= 1
            self.mc += 1

        for n in ins:
            del self.nodes[n].out_neighbors[node_id]
            self.edge_size -= 1
            self.mc += 1

        self.node_size -= 1
        self.mc += 1
        del self.nodes[node_id]

        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """

        if node_id2 in self.nodes[node_id1].out_neighbors:

            del self.nodes[node_id1].out_neighbors[node_id2]
            del self.nodes[node_id2].in_neighbors[node_id1]

            self.edge_size -= 1
            self.mc += 1

            return True

        return False

    # toString() in Java
    def __repr__(self):
        return "|V|={} , |E|={}".format(self.v_size(), self.e_size())