think(0)
def turn_around():
    turn_left()
    turn_left()
def grab_all_plant():
    plant = [[], [], [], []]
    x = 0
    while x<4:
        while object_here():
            if object_here("daisy"):
                take("daisy")
                plant[x].append("daisy")
            elif object_here("tulip"):
                take("tulip")
                plant[x].append("tulip")
        x+=1
        move()
    return plant
def move_with_range(x):
    for _ in range(x):
        move()
def put_all_plant():
    for door in range(len(next_plant)):
        while next_plant[door]:           
            flower = next_plant[door].pop(0) 
            put(flower)
        move()
turn_left()
move()
turn_left()
x=0
while front_is_clear():
    move()
turn_around()
next_plant = grab_all_plant()
print(next_plant)
while not at_goal():
    move()
move()
put_all_plant()
turn_around()
print(next_plant)
while not at_goal():
    move()
