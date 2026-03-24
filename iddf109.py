class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def DLS(node, goal, limit):
    if node.value == goal:
        return True
    
    if limit <= 0:
        return False
    
    for child in node.children:
        if DLS(child, goal, limit - 1):
            return True
    
    return False


def IDDFS(start, goal):
    depth = 0
    
    while depth < 10:   # limit to avoid infinite loop
        if DLS(start, goal, depth):
            return True
        depth += 1
    
    return False


# 🌳 Create tree
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

A.children = [B, C]
B.children = [D, E]

# ▶️ Call function and print output
result = IDDFS(A, 'E')
print("Goal Found:", result)