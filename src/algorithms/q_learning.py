import random

def q_learning(
    network,
    start,
    goal,
    episodes,
    learning_rate,
    discount_factor,
    exploration_prob,
    max_steps
):
    q_table = {}
    for node in network.get_nodes():
        q_table[node] = {}
        for neighbor in network.get_neighbors(node):
            q_table[node][neighbor] = 0

    for episode in range(episodes):
        current_state = start
        for _ in range(max_steps):
            if current_state == goal:
                break
            neighbor_nodes = list(network.get_neighbors(current_state))

            # Action
            if random.random() < exploration_prob:
                action = random.choice(neighbor_nodes) # Exploration
            else:
                action = max(neighbor_nodes, key=lambda x: q_table[current_state][x]) # Exploitation

            next_node = action
            edge_cost = network.get_edge_cost(current_state, next_node)
            reward = -edge_cost


            if next_node == goal:
                reward += 100
                next_q = 0
            else:
                next_q = max(q_table[next_node].values())

            q_table[current_state][next_node] = q_table[current_state][next_node] + learning_rate * (reward + discount_factor * next_q - q_table[current_state][next_node])
            current_state = next_node

    return q_table

def get_q_path(q_table, start, goal):

    path = [start]
    current = start

    while current != goal:

        if current not in q_table:
            return None

        if not q_table[current]:
            return None

        # Choose the action with the highest Q-value
        next_node = max(
            q_table[current],
            key=q_table[current].get
        )

        # Prevent infinite loops
        if next_node in path:
            return None

        path.append(next_node)

        current = next_node

    return path

def get_q_path_cost(network, path):
    cost = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]

        cost += network.get_edge_cost(current, next_node)

    return cost