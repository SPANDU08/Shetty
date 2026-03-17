
# Simple Reflex Agent for Vacuum Cleaner World

# Function to simulate the vacuum cleaner agent
def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

# Test the reflex agent
# Environment: location A is dirty, location B is clean initially
location = "A"
status = "Dirty"

# Define locations
locations = ["A", "B"]

# Simulate agent actions
for _ in range(5):  # Simulate for 5 iterations
    # Agent's action
    action = reflex_vacuum_agent(location, status)
    print(f"Location: {location}, Status: {status}, Action: {action}")

    # Update status
    if action == "Suck":
        status = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"