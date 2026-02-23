think(0)
def turn_right():
    for i in range(3):
        turn_left()

def turn_around(right=True):
    turn_right() if right else turn_left() 
    move()
    turn_right() if right else turn_left()

x=1; y=1
while front_is_clear():
    move()
    x+=1
    if 2<y<9 and 2<x<9:
        if object_here():
            while object_here():
                take()
    elif y>8:
        for _ in range(7):
            move()
        turn_right()
        for _ in range(8):
            move()
        while carries_object():
            put()
        done()
    if wall_in_front():
        if y%2==1:
            turn_around(right=False)
            y+=1; x=1
        else:
            turn_around(right=True)
            y+=1; x=1