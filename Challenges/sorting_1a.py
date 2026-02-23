think(0)
set_max_nb_steps(2000)
def turn_right():
    for _ in range(3):
        turn_left()
        
def turn_around():
    turn_left()
    turn_left()

def turn_back():
    turn_left();turn_left()
    while not wall_in_front():
        move()
        
def count_per_column():
    i=0
    while object_here():
        take()
        i+=1
        move()
    turn_back()
    return i

def put_per_column(col):
    total = len(col)
    for i in range(total):
        for _ in range(col[i]):
            put()
            move()
        turn_back()
        turn_right()
        if not wall_in_front():
            move()
        else: 
            done()
        turn_right()
x=0
each_col = []        
while front_is_clear():
    if object_here():
        move()
        x+=1        
    else:
        turn_around()
        break
for _ in range(x):
    move()
    turn_right()
    col = count_per_column()
    each_col.append(col)
    turn_right()
sorted_each_col = sorted(each_col, reverse=True)
print(sorted_each_col)
turn_around()
for _ in range(x-1):
    move()
turn_left()
put_per_column(sorted_each_col)


    
    