think(0)
def turn_right():
    for i in range(3):
        turn_left()
def move_to_goal():
    while not at_goal():
        if wall_in_front():
            turn_left()
        else:
            move()
    turn_left()
def u_turn(left=True):
    turn_left() if left else turn_right()
    if wall_in_front():
        if left==True:
            while carries_object():
                put()
            move_to_goal()
        else:
            turn_right()
            while not wall_in_front():
                move()
            while carries_object():
                put()
            move_to_goal()
    else:
        move()
        turn_left() if left else turn_right()
move_to_goal()
move()
y=1
while not at_goal():
    while object_here():
        take()
    if wall_in_front():
        if y%2==1:
            u_turn(left=True)
            y+=1
        else:
            u_turn(left=False)
            y+=1
    else:
        move()