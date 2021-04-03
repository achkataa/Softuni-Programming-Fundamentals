rooms = int(input())
chairs = 0
free_chairs = 0
clean_rooms = 0
for room in range(1, rooms + 1):
    room_chairs = [chair for chair in input().split()]

    chairs_x = room_chairs[0]
    taken_chairs = int(room_chairs[1])

    for x in chairs_x:
        chairs += 1

    if chairs < taken_chairs:
        print(f"{taken_chairs - chairs} more chairs needed in room {room}")
    else:
        free_chairs += chairs - taken_chairs
        clean_rooms += 1
    chairs = 0

if clean_rooms == rooms:
    print(f"Game On, {free_chairs} free chairs left")


