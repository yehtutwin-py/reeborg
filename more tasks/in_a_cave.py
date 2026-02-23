think(0)
def check_clear():
    if not front_is_clear() & wall_on_right():
        done()
    else:
        move()
def come_back():
    turn_left();turn_left()
    while front_is_clear():
        move()
    turn_left()
x=1    
while not wall_in_front() & wall_on_right():
    if x%2==1:
        turn_left()
        while front_is_clear():
            put()
            move()
        come_back()
        check_clear()
        x+=1
    else:
        move()
        x+=1
    