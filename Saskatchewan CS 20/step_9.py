think(0)
def turn_around():
    turn_left()
    turn_left()
move()    
while not at_goal():
    if wall_in_front():
        turn_around()
    move()
    if wall_in_front() and at_goal():
        turn_around();move()
        while carries_object():
            put()
        turn_around();move()
    while object_here():
        take()

