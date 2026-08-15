from network.network import Network
from algorithms.dijkstra import dijkstra
from algorithms.q_learning import q_learning, get_q_path, get_q_path_cost


def create_network():
    network = Network()

    for node in ["A", "B", "C", "D", "E", "F"]:
        network.add_node(node)

    network.add_edge("A", "B", weight=4)
    network.add_edge("A", "C", weight=2)

    network.add_edge("B", "D", weight=3)
    network.add_edge("C", "D", weight=1)

    network.add_edge("B", "E", weight=5)
    network.add_edge("D", "E", weight=2)

    network.add_edge("D", "F", weight=4)
    network.add_edge("E", "F", weight=1)

    return network


def main():
    network = create_network()

    start = "A"
    goal = "F"

    # --------------------
    # Dijkstra
    # --------------------

    dijkstra_path, dijkstra_cost = dijkstra(
        network,
        start,
        goal
    )

    print("Dijkstra")
    print("Path:", dijkstra_path)
    print("Cost:", dijkstra_cost)

    # --------------------
    # Q-learning
    # --------------------

    q_table = q_learning(
        network,
        start,
        goal,
        episodes=5000,
        learning_rate=0.1,
        discount_factor=0.9,
        exploration_prob=0.2,
        max_steps = 20
    )

    q_path = get_q_path(
        q_table,
        start,
        goal
    )

    if q_path is None:
        print("\nQ-learning")
        print("No path found")
        return

    q_cost = get_q_path_cost(network, q_path)

    print("\nQ-learning")
    print("Path:", q_path)
    print("Cost:", q_cost)


if __name__ == "__main__":
    main()