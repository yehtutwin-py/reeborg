think(0)
def turn_around_or_move():
    if not wall_in_front():
        if wall_on_right():
            move()
        else:
            for i in range(3):
                turn_left()
            move()
    else:
        turn_left()
        
put()
for i in range(3):
    turn_around_or_move()
while not object_here():
    turn_around_or_move()
    if object_here():
        done()
