import random
from network.network import Network

def create_network(number_of_nodes,edge_prob, min_edge_cost, max_edge_cost, seed = None):
    """
    :param number_of_nodes: number of nodes in the network
    :param edge_prob: probability of edge being generated between two nodes
    :param min_edge_cost: the smallest edge weight
    :param max_edge_cost: the largest edge weight
    :param seed: tracks the networks generated
    :return: Network
    """

    random.seed(seed)
    network = Network()
    nodes = [f"R{i}" for i in range(1, number_of_nodes + 1)]

    for node in nodes:
        network.add_node(node)

    #Ensure network is always connected
    for i in range(number_of_nodes - 1):
        network.add_edge(
            nodes[i],
            nodes[i + 1],
            weight = random.randint(min_edge_cost, max_edge_cost)
        )

    # Randomly add edges
    for i in network.get_nodes():
        for j in network.get_nodes():
            if i != j and not network.has_edge(i, j):
                if random.random() < edge_prob:
                    network.add_edge(
                        i,
                        j,
                        weight = random.randint(min_edge_cost, max_edge_cost))
    return network



