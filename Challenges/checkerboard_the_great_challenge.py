think(0)
x=1; y=1
def turn_right():
    for _ in range(3):
        turn_left()
        
def turn_around(left=True):
    turn_left() if left else turn_right()
    if wall_in_front():
        done()
    else:
        move()
        turn_left() if left else turn_right()      
while not wall_in_front():
    move()
    x+=1
z=x
turn_left()
turn_left()
while y<100:
    if y==(z/2) or y==(z/2)+1:
        move()
        if wall_in_front():
            if y%2==1:
                turn_around(left=False)
            else:
                turn_around(left=True)
            y+=1
    elif y%2==1:
        if x%2==1:
            put()
        x-=1; move()
        if wall_in_front():
            if x%2==1:
                put()
            turn_around(left=False)
            y+=1
    else:
        if x%2==0:
            put()
        x+=1; move()
        if wall_in_front():
            if x%2==0:
                put()
            turn_around(left=True)
            y+=1


    

        
        