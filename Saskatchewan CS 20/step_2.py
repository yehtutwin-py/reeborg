while not at_goal():
    move()
    if object_here():
        take()
    else:
        while carries_object():
            put()