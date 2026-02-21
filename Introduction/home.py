think(0)
def move_3():
    for i in range(3):
        move()    
        
def turn_right():
    for j in range(3):
        turn_left()
        
def move_or_turn(go=True):
    move_3() if go else turn_right()
    turn_left() if go else move()
    move_3() if go else turn_right()
    
for k in range(4):
    move_or_turn(go=True)
    if not k==3:
        move_or_turn(go=False)