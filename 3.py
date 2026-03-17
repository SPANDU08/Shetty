
def move_towards_goal(position, goal):
    while position < goal:
        position += 1
        print(f"Current Position: {position}")
    print("Reached the goal!")

# Set initial position and goal position
initial_position = 0
goal_position = 5

# Move towards the goal
move_towards_goal(initial_position, goal_position)