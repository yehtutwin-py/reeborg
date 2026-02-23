think(100)
x=1; y=1
def turn_right():
    for _ in range(3):
        turn_left()
while y<5:
    if y%2==1:
        if x%2==1:
            put()
        move()
        x+=1
        if wall_in_front():
            put()
            turn_left();
            if wall_in_front():
                done()
            else:
                move();turn_left()
            y+=1
    else:
        if x%2==0:
            put()
        x-=1; move()
        if wall_in_front():
            turn_right();
            if wall_in_front():
                done()
            else:
                move();turn_right()
            y+=1


    

        
        