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

world_size = size_of_world()
x,y = world_size
center_x = int((x+1)/2); center_y= int((y+1)/2)
while center_x!=x:
    move()
    x-=1
    if center_x==x:
        if center_y==y:
            put()
            done()
        turn_left()
        while center_y!=y:
            move()
            y-=1
            if center_y==y:
                put()
                done()
            