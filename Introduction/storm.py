think(0)
def pick_all():
    while object_here():
        take()

def turn_right():
    for i in range(3):
        turn_left()

def go_around():
    turn_right(); move()
    turn_left(); move(); move()
    turn_left(); move()
    turn_right()

def u_turn(left=True):
    turn_left() if left else turn_right()
    if not wall_in_front():
        move()
        turn_left() if left else turn_right()

def go_home():
    turn_left(); move()
    turn_right(); move(); move()
    turn_right(); move()   

def back_to_home_after_toss():
    turn_left()
    while not wall_in_front():
        move()
        if object_here():
            pick_all()
    while carries_object():
        toss()
    go_home()
    
y=1; move()
while not at_goal():
    while not wall_in_front():
        if object_here():
            pick_all()
        if front_is_clear():
            move()
            if object_here():
                pick_all()
        else: 
            go_around()
            if wall_in_front():
                turn_left(); move() 
                turn_left()
                y+=1
        if wall_in_front():
            if y%2==1:
                u_turn(left=True)
                if wall_in_front() & not right_is_clear():
                    turn_left()
                    while not wall_in_front():
                        move()
                    back_to_home_after_toss()
            elif wall_in_front() & not right_is_clear():
                back_to_home_after_toss()
            else:
                u_turn(left=False)
            y+=1           
            break

    
    

    
