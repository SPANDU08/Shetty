import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def enqueue(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def dequeue(self):
        return heapq.heappop(self.elements)[1]
    
    def is_empty(self):
        return len(self.elements) == 0


def uniform_cost_search(graph, start, goal):
    # Priority queue stores (cost, path)
    frontier = PriorityQueue()
    frontier.enqueue((start, [start]), 0)
    
    explored = {}
    
    while not frontier.is_empty():
        (current, path) = frontier.dequeue()
        cost_so_far = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
        
        if current == goal:
            return cost_so_far, path
        
        if current not in explored or cost_so_far < explored[current]:
            explored[current] = cost_so_far
            for neighbor, edge_cost in graph[current].items():
                new_path = path + [neighbor]
                new_cost = cost_so_far + edge_cost
                frontier.enqueue((neighbor, new_path), new_cost)
    
    return None


if __name__ == "__main__":
    # Define the graph
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'D': 1, 'E': 3},
        'C': {'F': 5},
        'D': {'G': 2},
        'E': {'G': 1},
        'F': {'G': 2},
        'G': {}
    }
    
    result = uniform_cost_search(graph, 'A', 'G')
    print("Cost and Path:", result)