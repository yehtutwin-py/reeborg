think(0)
def turn_around():
    turn_left()
    turn_left()
def grab_and_plant():
    if object_here():
        while object_here():
            take()
        for _ in range(8):
            move()
        while carries_object():
            put()
        turn_around()
def move_with_range(x):
    for _ in range(x):
        move()
        
turn_left()
move()
turn_left()
x=0
for i in range(4):
    while front_is_clear():
        move()
    turn_around()
    move_with_range(i)
    grab_and_plant()
while not at_goal():
    move()