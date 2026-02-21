think(0)
def turn_right():
    for i in range(3):
        turn_left()
        
def move_up():
    turn_left()
    move()
    turn_right()
   
x=0
take()
while x<3:
    move_up()
    move(); move()
    x+=1
put()
while object_here("token"):
    take("token")
    
turn_left(); turn_left()
while x>0:
    move(); move()
    move_up()
    x-=1