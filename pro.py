# Multi-Floor Car Parking System

floors = 4             # number of floors
slots_per_floor = 5   # slots in each floor

# create parking slots
parking = []
for f in range(floors):
    floor_slots = []
    for s in range(slots_per_floor):
        floor_slots.append(str(f+1) +str(s+1))   # e.g. "11", "12"
    parking.append(floor_slots)

while True:
    # display parking
    print("\nCurrent Parking Status:")
    for f in range(floors):
        print("Floor", f+1, ":", " ".join(parking[f]))

    choice = input("\nEnter floor and slot number to park (e.g., 1 2) or 'q' to quit: ")

    if choice.lower() == 'q':
        print("Exiting Parking System...")
        break

    parts = choice.split()
    if len(parts) != 2:
        print(" Please enter floor and slot number like: 1 2")
        continue

    floor_num = int(parts[0])
    slot_num = int(parts[1])

    # check valid floor/slot
    if floor_num < 1 or floor_num > floors or slot_num < 1 or slot_num > slots_per_floor:
        print(" Invalid floor or slot number!")
        continue

    # check if slot is free
    if parking[floor_num-1][slot_num-1] == 'X':
        print("That slot is already occupied!")
    else:
        parking[floor_num-1][slot_num-1] = 'X'
        print(" Car parked at Floor", floor_num, "Slot", slot_num)