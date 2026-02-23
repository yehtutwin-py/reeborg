think(0)
move() 
apple=0;carrot=0
while not at_goal():
    if wall_in_front():
        turn_left()
    if object_here("apple"):
        take("apple")
        apple+=1
    elif object_here("carrot"):
        take("carrot")
        carrot+=1
    move()
print(f"I counted {carrot} carrots and {apple} apples.")
done()