import networkx as nx

class Network:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, node_from, node_to, weight=1):
        self.graph.add_edge(node_from, node_to, weight=weight)

    def get_nodes(self):
        return self.graph.nodes

    def get_neighbors(self, node):
        return self.graph.neighbors(node)

    def get_edge_cost(self, node_from, node_to):
        return self.graph.edges[(node_from, node_to)]['weight']

    def get_path_cost(self, path):
        cost = 0
        for node_from, node_to in zip(path, path[1:]):
            cost += self.get_edge_cost(node_from, node_to)
        return cost

    def has_edge(self, node_from, node_to):
        return self.graph.has_edge(node_from, node_to)