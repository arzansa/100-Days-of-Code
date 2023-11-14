# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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

hurdles = 6
        
for i in range(hurdles):
    move()
    jump()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
