think(0)
def turn_right():
    for _ in range(3):
        turn_left()
        
def drop_apples():
    turn_left();turn_left()
    for _ in range(3):
        move()
    turn_left()
    for _ in range(2):
        for _ in range(4):
            move()
        turn_left()
    while carries_object():
        put()
        
def go_goal():
    turn_left()
    for i in range(2):
        for j in range(4):
            move()
        turn_right() if i==0 else turn_left()
    move();move()
    turn_right()
    move()
while not at_goal():
    if wall_in_front():
        turn_left()
    else: 
        move()
    while object_here():
        take()
    while carries_object():
        drop_apples()
        go_goal()