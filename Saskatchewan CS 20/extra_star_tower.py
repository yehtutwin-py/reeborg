think(0)
x=1
def check_wall():
    if wall_in_front() & wall_on_right():
            done()
    else:
        move()
def come_back():
    turn_left();turn_left()
    while not wall_in_front():
        move()
    turn_left()
turn_left()
while not wall_in_front() & not wall_on_right():
    if x%2==1:
        while not wall_in_front():
            put()
            move()
        come_back()
        check_wall()
        x+=1
    else:
        check_wall()
        turn_left()
        x+=1
    