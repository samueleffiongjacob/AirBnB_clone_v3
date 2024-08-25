#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

# Create a new state if no state objects exist
if storage.count(State) == 0:
    new_state = State(name="Test State")
    storage.new(new_state)
    storage.save()

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

# Get the first state's ID safely
state_objects = list(storage.all(State).values())
if state_objects:
    first_state_id = state_objects[0].id
    print("First state: {}".format(storage.get(State, first_state_id)))
else:
    print("No State objects found.")



# #!/usr/bin/python3
# """ Test .get() and .count() methods
# """
# from models import storage
# from models.state import State

# print("All objects: {}".format(storage.count()))
# print("State objects: {}".format(storage.count(State)))

# first_state_id = list(storage.all(State).values())[0].id
# print("First state: {}".format(storage.get(State, first_state_id)))