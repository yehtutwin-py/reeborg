think(0);x=0
def turn_right():
    for i in range(3):
        turn_left()
while not at_goal():
    if wall_in_front() & right_is_clear():
        turn_right()
    elif wall_in_front():
        turn_left()
    else: 
        move()
    if object_here("dandelion"):
        take() 
        pause()
        if x==0:
            turn_right()
            for i in range(4):
                move()
            put()
            turn_right();move()
            x+=1
        else: 
            turn_right();move();move()
            turn_left();move();move();move()
            put(); move()
            
