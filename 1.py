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
# Environment: location A is dirty, location B is clean
location = "A"
status = "Dirty"

# Agent's action
action = reflex_vacuum_agent(location, status)
print(f"Location: {location}, Status: {status}, Action: {action}")