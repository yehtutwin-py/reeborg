think(0)
def turn_right():
    for _ in range(3):
        turn_left()
        
put(); move()
while not object_here():
    if not front_is_clear():
        if right_is_clear():
            turn_right()
        else:
            turn_left()
    else:
        move()
done()