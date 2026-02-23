think(0)
put();move()
while not object_here():
    if wall_in_front():
        turn_left()
    else:
        move()
done()