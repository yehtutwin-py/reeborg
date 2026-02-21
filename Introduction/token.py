think(0)
while not at_goal():
    if not object_here():
        while carries_object():
            put()
        move()
        if at_goal():
            done()
    while object_here():
        take()
    move()