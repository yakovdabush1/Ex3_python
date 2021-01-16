import random


class Node_Data:

    def __init__(self, key, info="", tag=0, pos=None):
        self.key = key
        self.info = info
        self.tag = tag
        self.pos = pos

        # this is all out edges
        self.out_neighbors = {}
        # this is all in edges
        self.in_neighbors = {}

    def update_position(self, v_size):
        if self.pos is None:
            x, y, z = random.uniform(0, v_size), random.uniform(0, v_size), 0
            self.pos = (x, y, z)

    def __repr__(self):
        return "{}: |edges out| {} |edges in| {}".format(self.key, len(self.out_neighbors), len(self.in_neighbors))
