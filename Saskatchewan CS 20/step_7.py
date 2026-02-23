think(0)
def turn_right():
    for _ in range(3):
        turn_left()
def move_left():
    move();turn_left()
def move_put():
    move();put()
def draw_one():
    for _ in range(5):
        move_put()
    turn_right(); move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
        
def draw_zero():
    for _ in range(5):
        move_put()
    turn_right()
    move_put()
    move_put()
    turn_right()
    for _ in range(4):
        move_put()
    turn_right()
    move_put()  
    turn_left()
    move_left()
    
move_left()
draw_one()
move_left()
draw_zero()
for _ in range(3):
    move()
turn_left()
draw_zero()
for _ in range(3):
    move()
turn_left()
draw_one()
move_left()
draw_zero()
while not at_goal():
    move()