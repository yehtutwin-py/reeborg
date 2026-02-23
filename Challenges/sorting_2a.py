think(100)
col=[]; x=0
def put_items(items):
    for i in items:
        for _ in range(i):
            put()
        if wall_in_front():
            done()
        else:
            move()
        
while len(col)<9:
    x=0
    while object_here():
        take(); x+=1
    col.append(x)
    move()
    if not object_here():
        turn_left();turn_left();move()
        break
new_col = (sorted(col, reverse=True))
put_items(new_col)

    

        
        