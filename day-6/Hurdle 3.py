# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
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
