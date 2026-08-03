# Vacuum Cleaner Problem

# Initial state of rooms
rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Vacuum starts in Room A
location = 'A'

while True:
    print("\nVacuum is in Room", location)

    if rooms[location] == 'Dirty':
        print("Room", location, "is Dirty -> Cleaning...")
        rooms[location] = 'Clean'
    else:
        print("Room", location, "is already Clean.")

    # Check if all rooms are clean
    if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
        print("\nAll rooms are clean.")
        break

    # Move to the other room
    if location == 'A':
        location = 'B'
    else:
        location = 'A'

print("\nFinal Room Status:")
print(rooms)
