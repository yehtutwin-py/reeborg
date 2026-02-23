think(0)
set_max_nb_steps(2000)
def turn_right():
    for i in range(3):
        turn_left()
def turn_around():
    turn_left();turn_left()
    move()  
take()
while front_is_clear():
    move()
    if not object_here():
        turn_around()
        turn_left()
        move()
        if not object_here():
            turn_around()
            move()
            if not object_here():
                turn_around()
                turn_left()
                done()
    if object_here():
        take()

        
    