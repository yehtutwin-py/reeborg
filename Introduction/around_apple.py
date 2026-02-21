think(0)
move()
while not at_goal():
    if object_here():
        take()
    else:
        if not wall_in_front():
            move()
        else:
            turn_left()