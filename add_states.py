#!/usr/bin/python3
"""
Script to add multiple State objects to the database for testing
"""

from models import storage
from models.state import State

# Create and add new State objects
states = [
    State(name="California"),
    State(name="New York"),
    State(name="Texas"),
    State(name="Florida"),
    State(name="Arizona"),
    State(name="Colorado"),
    State(name="Nevada"),
    State(name="Oregon"),
    State(name="Washington"),
    State(name="Alaska")
]

for state in states:
    storage.new(state)

# Save all changes to the database
storage.save()

print("States added successfully!")




# #!/usr/bin/python3
# """
# Script to add multiple State objects to the database for testing
# """

# from models import storage
# from models.state import State

# # Create and add new State objects
# state_1 = State(name="California")
# state_2 = State(name="New York")
# state_3 = State(name="Texas")
# state_4 = State(name="Florida")
# state_5 = State(name="Arizona")
# state_6 = State(name="Colorado")
# state_7 = State(name="Nevada")
# state_8 = State(name="Oregon")
# state_9 = State(name="Washington")
# state_10 = State(name="Alaska")

# # Add the states to the storage engine
# storage.new(state_1)
# storage.new(state_2)
# storage.new(state_3)
# storage.new(state_4)
# storage.new(state_5)
# storage.new(state_6)
# storage.new(state_7)
# storage.new(state_8)
# storage.new(state_9)
# storage.new(state_10)

# # Save all changes to the database
# storage.save()

# print("States added successfully!")
