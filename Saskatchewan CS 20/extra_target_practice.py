think(0)
set_max_nb_steps(2000)
def turn_right():
    for _ in range(3):
        turn_left()

def move_put():
    move()
    put()

def turn_around():
    turn_left()
    turn_left()

def u_turn(left=True):
    turn_left() if left else turn_right()
    move()
    turn_left() if left else turn_right()

def find_object_center():
    x=1;y=1; total_x=1
    while not object_here():
        if wall_in_front():
            break
        else:
            move()
        total_x+=1
    x=total_x
    while not object_here():
        if wall_in_front():
            if y%2==1:
                u_turn(left=True)
            else:
                u_turn(left=False)
            y+=1; x=1         
        else:
            move()
            x+=1
    if y%2==0:
        x=total_x-x+1
    return x,y
def prepare():
    while not wall_in_front():
        move()
    if wall_in_front():
        turn_around()
        
def put_item_line(line):
    z=1
    while not wall_in_front():  
        if z==line:
            move_put()
        elif object_here():
            move_put()
        else:
            put();move()
        z+=1
    turn_around()
    while line!=z:
        move()
        z-=1
object_location = find_object_center()
x,y = object_location
if not is_facing_north():
    if y%2==1:
        turn_right()
    else:
        turn_left()
prepare()   
put_item_line(y)
turn_right()
prepare()
put_item_line(x)