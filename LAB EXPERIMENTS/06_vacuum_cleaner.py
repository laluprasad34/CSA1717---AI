# Simple Vacuum Cleaner agent
rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

while "Dirty" in rooms.values():
    if rooms[location] == "Dirty":
        print("Room", location, "is dirty. Suck.")
        rooms[location] = "Clean"
    elif location == "A":
        print("Move right")
        location = "B"
    else:
        print("Move left")
        location = "A"

print("All rooms are clean:", rooms)
