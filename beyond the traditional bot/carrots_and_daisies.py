think(0)
move()       
while not at_goal():
    move()
    if wall_in_front():
        turn_left()
    if object_here("daisy"):
        print("I am not picking it up; I prefer carrots!")
    elif object_here("carrot"):
        take("carrot")