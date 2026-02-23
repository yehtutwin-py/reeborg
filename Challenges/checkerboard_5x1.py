think(100)
x=0
while front_is_clear():
    x+=1
    if x%2==1:
        put()
    move()
    if wall_in_front():
        put()
        done()

    

        
        