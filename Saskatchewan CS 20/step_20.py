think(0)
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def wall_build_if_between_walls():
    turn_around()
    move()
    turn_left()
    build_wall()
    turn_left()
    
for i in range(3):
    move()
turn_right()
while not wall_in_front():
    if wall_on_right():
        move()
        if at_goal():
            done()
        if right_is_clear():
            move()
            if wall_on_right():
                wall_build_if_between_walls()
            else:
                turn_around()
                move()
                turn_left()
                if wall_in_front() and wall_on_right():
                    turn_left()
        elif wall_in_front() and wall_on_right():
            turn_left()
    elif front_is_clear():
        move()
        if not front_is_clear():
            turn_left()