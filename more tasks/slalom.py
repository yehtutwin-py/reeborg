think(0)
def turn_right():
    for _ in range(3):
        turn_left()
def zig_zag(zig=True):
    move();move()
    turn_right() if zig else turn_left()
    move();move()
    turn_left() if zig else turn_right()
x=0  
move();move()
turn_left();move()
turn_right()
for _ in range(9):
    if x%2==0:
        zig_zag(zig=True)
    else:
        zig_zag(zig=False)
    x+=1
while not at_goal():
    move()