think(0)
x=1; y=1
def size_of_world():
    x=1; y=1
    while front_is_clear():
        move()
        x+=1
        if not front_is_clear():
            turn_left()
            while front_is_clear():
                move()
                y+=1
    turn_left()
    return x,y
def turn_move(left=True):
    turn_left() if left else turn_right()
    move()
    put()
def put_item(x):
    put()
    for _ in range(x):
        turn_move(left=True)
world_size = size_of_world()
x,y = world_size
y_max = y
center_x = int((x+1)/2); center_y= int((y+1)/2)
print
while center_x!=x:
    move()
    x-=1
    if center_x==x:
        if center_y==y:
            put()
            turn_left();
            turn_move()
            done()
        turn_left()
        while center_y!=y:
            move()
            y-=1
            if center_y==y:
                put_item(3)
                done()
                    
            