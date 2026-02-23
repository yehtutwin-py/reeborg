think(0)
def turn_right():
    for _ in range(3):
        turn_left()
move();turn_right()
move()
while not at_goal():
    if wall_in_front():
        turn_left()
    elif right_is_clear():
        turn_right()
        build_wall()
        turn_left()
    else:
        move()