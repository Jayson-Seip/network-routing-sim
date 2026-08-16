from network.network import Network
from algorithms.dijkstra import dijkstra
from algorithms.q_learning import q_learning, get_q_path, get_q_path_cost
from network.network_generator import create_network


def main():
    network = create_network(
        10, 0.25, 1, 8,3
    )

    start = "R1"
    goal = "R9"

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