think(20)
def turn_right():
    for i in range(3):
        turn_left()
def move_turn(left=True):
    turn_left() if left else turn_right()
    move()
    turn_right() if left else turn_left()
def climb_up():
    move_turn(left=True)
    move();move()
def climb_down():
    move();move()
    move_turn(left=True)
take("star")
for i in range(5):
    climb_up()
    if object_here():
        while object_here("token"):
            take("token")
        put("star")
        turn_left();turn_left()
        for j in range(i+1):
            climb_down()
        done()
    