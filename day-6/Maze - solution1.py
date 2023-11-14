# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# not optimal because robot does a full circle every square

def turn_right():
    for i in range(3):
        turn_left()  

while not at_goal():
    if not front_is_clear():
        turn_left()
    else:
        move()
        turn_right()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
