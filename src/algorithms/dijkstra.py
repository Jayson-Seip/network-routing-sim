import heapq

def dijkstra(network, start, goal):
    distances = {node: float("inf") for node in network.get_nodes()}
    predecessors = {node: None for node in network.get_nodes()}
    pq = []

    distances[start] = 0
    heapq.heappush(pq, (distances[start], start))

    while pq:
        distance, current = heapq.heappop(pq)

        if distance > distances[current]:
            continue

        if current == goal:
            break

        for neighbor in network.get_neighbors(current):

            cost = network.get_edge_cost(current, neighbor)
            if cost < 0:
                raise ValueError("Negative Weights are not supported")

            new_distance = distance + cost

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current
                heapq.heappush(pq, (new_distance, neighbor))

    if distances[goal] == float("inf"):
        print("No Path Found")
        return None, float("inf")

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = predecessors[current]

    path.reverse()

    return path, distances[goal]

