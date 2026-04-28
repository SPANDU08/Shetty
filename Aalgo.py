import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        current_f, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return reconstruct_path(parent, current_node)

        for neighbor, weight in graph[current_node]:
            tentative_g = g_cost[current_node] + weight

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current_node

    return None


def reconstruct_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Graph
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((0, 2), 1), ((1, 1), 1)],
    (0, 2): [((0, 1), 1), ((1, 2), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1), ((1, 2), 1)],
    (1, 2): [((1, 1), 1), ((0, 2), 1)]
}

start = (0, 0)
goal = (1, 2)

path = a_star(graph, start, goal, heuristic)
print("Shortest path:", path)