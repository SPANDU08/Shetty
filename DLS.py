# Depth Limited Search (DLS) implementation in Python

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dls(self, start, goal, limit):
        return self._dls_recursive(start, goal, limit)

    def _dls_recursive(self, node, goal, limit):
        print(f"Visiting: {node}, Depth limit: {limit}")
        if node == goal:
            return True
        if limit <= 0:
            return False
        if node not in self.graph:
            return False

        for neighbor in self.graph[node]:
            if self._dls_recursive(neighbor, goal, limit - 1):
                return True
        return False


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    g.add_edge("D", "F")

    start_node = "A"
    goal_node = "F"
    depth_limit = 3

    print(f"\nSearching for {goal_node} starting from {start_node} with depth limit {depth_limit}...\n")
    found = g.dls(start_node, goal_node, depth_limit)

    if found:
        print(f"Goal {goal_node} found within depth limit {depth_limit}.")
    else:
        print(f"Goal {goal_node} NOT found within depth limit {depth_limit}.")
