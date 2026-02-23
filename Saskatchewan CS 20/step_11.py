think(0)
repeat 23:
    if wall_in_front():
        turn_left()
    else:
        move()
    while object_here():
        take()