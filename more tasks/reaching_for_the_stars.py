think(0)
def check_wall():
    if wall_in_front() & wall_on_right():
            done()
def come_back():
    turn_left();turn_left()
    while not wall_in_front():
        move()
    turn_left()
x=1;y=1
while not wall_in_front() & not wall_on_right():
    if x%4==0:
        turn_left()
        while y<11:
            put()
            if y==10:
                come_back()
            else:
                move()
            y+=1
        y=1
    check_wall()
    move()
    x+=1
    