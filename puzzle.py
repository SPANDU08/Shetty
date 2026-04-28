import heapq

# Goal state
GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

# Directions for movement
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))

    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == GOAL:
            return path + [current]

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [current])
                )

    return None


def print_solution(solution):
    for step in solution:
        for row in step:
            print(row)
        print("-----")


# Example start state
start_state = ((1, 2, 3),
               (4, 0, 6),
               (7, 5, 8))

solution = a_star(start_state)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")
    print_solution(solution)
else:
    print("No solution exists.")