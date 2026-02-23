think(0)
set_max_nb_steps(2000)
while not object_here():
    move()
x=0
while object_here():
    take()
    x+=1
move()
total=x;x=0
while x!=(total*2):
    put()
    x+=1