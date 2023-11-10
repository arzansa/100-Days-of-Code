import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

ascii_treasure='''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
'''

ascii_map='''
    ___
    ).x)
   (:_(
'''

ascii_pirate1="""
         _,-._
        ; ___ :          
    ,--' (. .) '--.__     ,------------------------------.
  _;      |||        \   |             Argh!             |
 '._,-----''';=.____,"   |       What be ye called,      |
   /// < o>   |##|       |          landlubber?          |
   (o        \`--'       //`-----------------------------'
  ///\ >>>>  _\ <<<<    //
 --._>>>>>>>><<<<<<<<  / 
 ___() >>>[||||]<<<<
 `--'>>>>>>>><<<<<<<
      >>>>>>><<<<<<
        >>>>><<<<<
         >>ctr<<
"""

ascii_pirate2="""
         _,-._
        ; ___ :          
    ,--' (. .) '--.__     ,------------------------------.
  _;      |||        \   |           Aye. Well,          |
 '._,-----''';=.____,"   |      let's be goin' then.     |
   /// < o>   |##|       |    The ship sets sail soon!   |
   (o        \`--'       //`-----------------------------'
  ///\ >>>>  _\ <<<<    //
 --._>>>>>>>><<<<<<<<  / 
 ___() >>>[||||]<<<<
 `--'>>>>>>>><<<<<<<
      >>>>>>><<<<<<
        >>>>><<<<<
         >>ctr<<
"""

ascii_ship = '''
#############################################################################
#(@@@@)                    (#########)                   (@@@@@@@@(@@@@@@@@@#
#@@@@@@)___                 (####)~~~   /\                ~~(@@@@@@@(@@@@@@@#
#@@@@@@@@@@)                 ~~~~      /::~-__               ~~~(@@@@@@@@)~~#
#@@@)~~~~~~                           /::::::/\                  ~~(@@@@)   #
#~~~                              O  /::::::/::~--,                 ~~~~    #
#                                 | /:::::/::::::/{                         #
#                 |\              |/::::/::::::/:::|                        #
#                |:/~\           ||:::/:::::/::::::|                        #
#               |,/:::\          ||/'::: /::::::::::|                       #
#              |#__--~~\        |'#::,,/::::::::: __|   ,,'`,               #
#             |__# :::::\       |-#"":::::::__--~~::| ,'     ',     ,,      #
#,    ,,     |____#~~~--\,'',.  |_#____---~~:::::::::|         ',','  ',    #
# '.,'  '.,,'|::::##~~~--\    `,||#|::::::_____----~~~|         ,,,     '.''#
#____________'----###__:::\_____||#|--~~~~::::: ____--~______,,''___________#
#^^^  ^^^^^   |#######\~~~^^O, | ### __-----~~~~_____########'  ^^^^  ^^^   #
#,^^^^^','^^^^,|#########\_||\__O###~_######___###########;' ^^^^  ^^^   ^^ #
#^^/\/^^^^/\/\^^|#######################################;'/\/\/^^^/\/^^^/\/^#
#   /\/\/\/\/\  /\|####################################'      /\/\/\/\/\    #
#\/\/\     /\/\/\  /\/\/\/\    /\/\/\/\/\   /\/\/\    /\/\/\/\      /\/\/\/\#
#spb\/\/\    /\/\/\/\    /\/\/\/\    /\/\/\/\   /\/\/\/\    /\/\/\/\/\      #
#############################################################################
'''

ascii_island = '''
                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     |
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.                  
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 '''

ascii_monster = """
                                             ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L'
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `/
                -,-..\  _  \  `  /  ,  / `._) _,-\`       |
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               |
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
"""

ascii_lightning = '''
           ___(                        )
          (                          _)
         (_                       __))
           ((                _____)
             (_________)----'
                _/  /
               /  _/
             _/  /
            / __/
          _/ /
         /__/
        //
       /'
       '''

ascii_cave = '''
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 88888888888888888888888888888888888888888888888888888888888888888 88
'''

ascii_goblin = """
             ,      ,
            /(.-""-.)/
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   |
           \ \__/\__/ /
         ___\ \|--|/ /___
       /`    \      /    `|
      /       '----'      /
"""

ascii_door1 = """
      ______
   ,-' ;  ! `-.
  / :  !  :  . |
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |_____;----.___|
"""

ascii_door2 = """
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
"""

ascii_gargoyle = """
                                  _.-.
                                 ._.-.|
                    .^         _.-'=. ||
                  .'  )    .-._.-=-..' |'.
               .'   .'   _.--._-='.'   |  `.  ^.
             .'   .'    _`.-.`=-./'.-. / .-.\ `. `.
           .'    /      _.-=-=-/ | '._)`(_.'|   \  `.
          /    /|       _.--=.'  `. (.-v-.)/    |\   |
        .'    / \       _.-.' \-.' `-..-..'     / \   `.
       /     /   `-.._ .-.'      `.'  " ". _..-'  |    |
"""
ascii_door3 = """
 ______________
|\ ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+-+-| | |
| | |_|_|_|_| | |
| |     ___   | |
| |    /__/   | |
| |   [%==] ()| |
| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|___________|_|
"""

score = 0

clear()
print(ascii_pirate1)
name = input('What is your name?:\n')

clear()

print(ascii_pirate2)
input(f'Welcome to the crew, {name}! (Press enter to continue)')

clear()

print(ascii_map)

choice = ''

while choice != 'a' and choice != 'b':
    print('The captain hands you a map. He wants you to read it and tell him which direction to go.')
    print("a. Go West.")
    print("b. go Northeast.")
    choice = input()
    clear()
    if (choice != 'a' and choice != 'b'):
        print(ascii_map)
        print("Please enter a valid choice.")

score += 1

if choice == 'a':
    print(ascii_ship)
    input("The crew gathers onboard and sets sail Westward. (Press enter to continue)")
    clear()
    print(ascii_monster)
    print("The crew sails into a foggy abyss. A monster leaps out from the fog! He wrecks the ship, and it sinks into the sea... (GAME OVER.)")
    print(f'Name: {name}')
    print(f'Score: {score}')

    exit()

if choice == 'b':
    print(ascii_ship)
    input("The crew gathers onboard and sets sail to the Northeast. (Press enter to continue)")
    clear()
    print(ascii_island)
    print("the ship comes upon an island, but the wind is too heavy, and the ship can't make it the rest of the way to shore.")
  

choice = ''

while choice != 'a' and choice != 'b':
    print('Would you like to swim to shore or stay back with the crew?')
    print("a. Wait with the crew.")
    print("b. Swim to shore!")
    choice = input()

    if (choice != 'a' and choice != 'b'):
        print(ascii_island)
        print("Please enter a valid choice.")

score += 1

if choice == 'a':
    clear()
    print(ascii_lightning)
    input("You wait a couple hours, and a terrible storm starts to brew. The ship is struck by lightning, and catches fire! (GAME OVER.)")
    print(f'Name: {name}')
    print(f'Score: {score}')
    exit()

if choice == 'b':
    clear()
    print(ascii_island)
    print("You swim ashore, and find a small cave entrance!")
    
choice = ''

while choice != 'a' and choice != 'b' and choice != 'c':
    clear()
    print(ascii_cave)
    print("You enter the cave, and come up a hallway with 3 doors. Which way would you like to go?")
    print("a. Left door.")
    print('b. Right door.')
    print("c. Forward!")
    choice = input()

    if (choice != 'a' and choice != 'b' and choice != 'c'):
        print(ascii_cave)
        print("Please enter a valid choice.")

score += 1

if choice == 'a':
    clear()
    print(ascii_door3)
    input("You see a metal door. You grab the handle and sneak inside... (Press enter to continue)")
    clear()
    print(ascii_treasure)
    print("You find the treasure! Congratulations! You're gonna be rich... (YOU WIN!)")
    print(f'Name: {name}')
    score += 996
    input(f'Score: {score}')
    
    exit()

if choice == 'b':
    clear()
    print(ascii_door1)
    input("You come upon a heavy door and open it slowly... (Press enter to continue)")
    clear()
    print(ascii_goblin)
    print("A goblin is behind the door waiting for you. He slashes you with his sword! You are defeated... (GAME OVER.)")
    print(f'Name: {name}')
    input(f'Score: {score}')

    exit()

if choice == 'c':
    clear()
    print(ascii_cave)
    input("You walk forward and open the large door in from of you. You walk inside... (Press enter to continue)")
    clear()
    print(ascii_gargoyle)
    print("You are confronted by a gargoyle! He sure looks mad! He smashes you into tiny pieces. (GAME OVER.)")
    print(f'Name: {name}')
    input(f'Score: {score}')
  
    exit()


    



exit()



