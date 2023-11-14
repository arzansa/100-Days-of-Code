def jump():
    turn_left()
    move()
    turn_right()
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()  

while not at_goal():
    if not front_is_clear():
        jump()
    else:
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
