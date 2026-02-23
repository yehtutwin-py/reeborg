think(0)
turn_left()
col=0; col_array=[]; row=1
def turn_right():
    for i in range(3):
        turn_left()
        
def turn_back(left=True):
    turn_left()
    turn_left()
    while not wall_in_front():
        move()
    turn_left() if left else turn_right()
    
def put_per_column(col):
    total = len(col)
    for i in range(total):
        for _ in range(col[i]):
            put()
            move()
        turn_back(left=False)
        if not wall_in_front():
            move()
        else: 
            done()
        turn_right()
        
while row<10:
    while object_here():
        take()
        move()
        col+=1
    col_array.append(col)
    col=0
    turn_back(left=True)
    move()
    row+=1
    if not object_here():
        turn_left();turn_left()
        move()
        turn_right()
        break
    else:
        turn_left()
sorted_col_array = sorted(col_array)
put_per_column(sorted_col_array)
    
    

