think(0)

def turn_right():
    for _ in range(3):
        turn_left()

def turn_back(left=True):
    turn_left(); turn_left()
    while not wall_in_front():
        move()
    turn_left() if left else turn_right()

def put_columns(cols):
    for c in cols:
        for _ in range(c):
            put(); move()
        turn_back(False)
        if wall_in_front(): done()
        move(); turn_right()

cols = []
turn_left()

while len(cols) < 9:
    c = 0
    while object_here():
        take(); move(); c += 1
    cols.append(c)
    turn_back(True)
    move()
    if not object_here():
        turn_left(); turn_left(); move(); turn_right()
        break
    turn_left()

put_columns(sorted(cols))