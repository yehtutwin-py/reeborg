think(0)
def turn_right():
    for i in range(3):
        turn_left()
while not at_goal():
    if wall_in_front():
        if right_is_clear():
            turn_right()
        else:
            turn_left()
    else:
        move()