think(0)
def pick_up():
    move(); take()
def put_berries():
    turn_left();turn_left()
    move();move()
    put();put()
def pick_two_berries():
    pick_up()
    pick_up()
def turn_right():
    for i in range(3):
        turn_left()
def pick_berry_put(left=True):
    turn_left() if left else turn_right()
    pick_two_berries()
    put_berries()
    turn_left() if left else turn_right()
x=0
while not at_goal():
    move()
    while x<4:
        if x%2==0:
            pick_berry_put(left=True)
            x+=1
            break
        else:
            pick_berry_put(left=False)
            x+=1
            break
        