think(0)
def turn_right():
    for i in range(3):
        turn_left()

def turn_around(right=True):
    turn_right() if right else turn_left() 
    move()
    turn_right() if right else turn_left()
y=1
move();move()
while object_here():
    if object_here("apple"):
        fruit="apple"
    elif object_here("strawberry"):
        fruit="strawberry"
    elif object_here("banana"):
        fruit="banana"
    break
take(fruit)
while front_is_clear():
    move()
    while object_here(fruit):
        take(fruit)
    if y>8:
        done()
    if wall_in_front():
        if y%2==1:
            turn_around(right=False)
            y+=1
        else:
            turn_around(right=True)
            y+=1