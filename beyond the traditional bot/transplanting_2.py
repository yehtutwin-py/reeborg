think(0)
def turn_around():
    turn_left()
    turn_left()
def grab_all_plant():
    plant = []
    while not at_goal():
        if object_here():
            x=0
            while object_here():
                take()
                x+=1    
            plant.append(x)
            print(plant)
        move()
    return plant
def move_with_range(x):
    for _ in range(x):
        move()
        
turn_left()
move()
turn_left()
x=0
while front_is_clear():
    move()
turn_around()
next_plant = grab_all_plant()
move()
print(next_plant)
for i in next_plant:
    for _ in range(i):
        put()
    move()
turn_around()
while not at_goal():
    move()