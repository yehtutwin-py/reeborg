think(0)
def turn_right():
    for _ in range(3):
        turn_left()
def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump_hurdle()
    else:
        move()