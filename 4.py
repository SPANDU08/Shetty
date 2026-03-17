
# Rational Agent to move towards a goal

class RationalAgent:
    def __init__(self, goal):
        self.position = 0
        self.goal = goal
    
    def move_towards_goal(self):
        while self.position < self.goal:
            self.position += 1
            print(f"Current Position: {self.position}")
        print("Reached the goal!")

# Set a goal position
goal_position = 5

# Create a rational agent
agent = RationalAgent(goal_position)

# Move the agent towards the goal
agent.move_towards_goal()
