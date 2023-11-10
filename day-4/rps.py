import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

win = '''
 __   __  _______  __   __    _     _  ___   __    _  __         ___          ____   
|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | ||  |       |   |        |    |  
|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| ||  |       |___|  ____  |_    | 
|       ||  | |  ||  |_|  |  |       ||   | |       ||  |        ___  |____|   |   | 
|_     _||  |_|  ||       |  |       ||   | |  _    ||__|       |   |          |   | 
  |   |  |       ||       |  |   _   ||   | | | |   | __        |___|         _|   | 
  |___|  |_______||_______|  |__| |__||___| |_|  |__||__|                    |____|  
'''

lose = '''
 __   __  _______  __   __    ___      _______  _______  _______  __         ___           ____  
|  | |  ||       ||  | |  |  |   |    |       ||       ||       ||  |       |   |         |    | 
|  |_|  ||   _   ||  | |  |  |   |    |   _   ||  _____||    ___||  |       |___|  ____  |    _| 
|       ||  | |  ||  |_|  |  |   |    |  | |  || |_____ |   |___ |  |        ___  |____| |   |   
|_     _||  |_|  ||       |  |   |___ |  |_|  ||_____  ||    ___||__|       |   |        |   |   
  |   |  |       ||       |  |       ||       | _____| ||   |___  __        |___|        |   |_  
  |___|  |_______||_______|  |_______||_______||_______||_______||__|                     |____| 
'''

draw = '''
 ______   ______    _______  _     _  __         ___          ___  
|      | |    _ |  |   _   || | _ | ||  |       |   |        |   | 
|  _    ||   | ||  |  |_|  || || || ||  |       |___|  ____  |   | 
| | |   ||   |_||_ |       ||       ||  |        ___  |____| |   | 
| |_|   ||    __  ||       ||       ||__|       |   |        |   | 
|       ||   |  | ||   _   ||   _   | __        |___|        |   | 
|______| |___|  |_||__| |__||__| |__||__|                    |___| 
'''

while(True):

    choice = ''
    leave = ''

    while choice != '0' and choice != '1' and choice != '2':
        print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
        choice = input()

        if choice != '0' and choice != '1' and choice != '2':
            print("Please enter a valid choice.")

    choice = int(choice)
    cpu_choice = random.randint(0, 2)

    if (choice == cpu_choice):
        while (leave != 'y' and leave != 'n'):
            
            if choice == 0:
                              
                print(rock)
                print("YOU: rock")
                
                print(rock)
                print("COMPUTER: rock")
                
            if choice == 1:
                 
                print(paper)
                print("YOU: paper") 
                      
                print(paper)
                print("COMPUTER: paper")       

            if choice == 2:
                
                
                print(scissors)
                print("YOU: scissors")
                                
                print(scissors)
                print("COMPUTER: scissors")
            
            print('\n')
            print(draw)
            print("\n\nDraw!")

            print("Play again? y/n")
            leave = input()
            if leave != 'y' and leave != 'n':
                print("Please enter a valid choice.")
            if leave == 'n':
                print("Goodbye.")
                exit()
            elif leave == 'y':
                pass

    if (choice == 0 and cpu_choice == 1):
        while (leave != 'y' and leave != 'n'):
            
            print(rock)
            print("YOU: rock")

            
            print(paper)
            print("COMPUTER: paper")

            print('\n')
            
            print(lose)
            print('\n\nYou chose rock, computer chose paper.')
            print("\nYou lose! Play again? y/n")
            leave = input()
            if leave != 'y' and leave != 'n':
                print("Please enter a valid choice.")
            if leave == 'n':
                print("Goodbye.")
                exit()
            elif leave == 'y':
                pass

    if (choice == 0 and cpu_choice == 2):
        while (leave != 'y' and leave != 'n'):
            
            print(rock)
            print("YOU: rock")
            
            print(scissors)
            print("COMPUTER: scissors")
            
            print('\n')
            print(win)
            print('\n\nYou chose rock, computer chose scissors.')
            print("You win! Play again? y/n")
            leave = input()
            if leave != 'y' and leave != 'n':
                print("Please enter a valid choice.")
            if leave == 'n':
                print("Goodbye.")
                exit()
            elif leave == 'y':
                pass

    if (choice == 1 and cpu_choice == 0):
        while (leave != 'y' and leave != 'n'):
            print(paper)
            print("YOU: paper")
            
            print(rock)
            print("COMPUTER: rock")

            print('\n')
            print(win)
            print('\n\nYou chose paper, computer chose rock.')
            print("You win! Play again? y/n")
            leave = input()
            if leave != 'y' and leave != 'n':
                print("Please enter a valid choice.")
            if leave == 'n':
                print("Goodbye.")
                exit()
            elif leave == 'y':
                pass

    if (choice == 1 and cpu_choice == 2):
        while (leave != 'y' and leave != 'n'):
            
            
            print(paper)
            print("YOU: paper")
            
            print(scissors)
            print("COMPUTER: scissors")

            print('\n')
            print(lose)
            print('\n\nYou chose paper, computer chose scissors.')
            print("You lose! Play again? y/n")

            leave = input()
            if leave != 'y' and leave != 'n':
                print("Please enter a valid choice.")
            if leave == 'n':
                print("Goodbye.")
                exit()
            elif leave == 'y':
                pass

    if (choice == 2 and cpu_choice == 0):
        while (leave != 'y' and leave != 'n'):
            
            
            print(scissors)
            print("YOU: scissors")
            
            print(rock)
            print("COMPUTER: rock")

            print('\n')
            print(lose)
            print('\n\nYou chose scissors, computer chose rock.')
            print("You lose! Play again? y/n")

            leave = input()
            if leave != 'y' and leave != 'n':
                print("Please enter a valid choice.")
            if leave == 'n':
                print("Goodbye.")
                exit()
            elif leave == 'y':
                pass

    if (choice == 2 and cpu_choice == 1):
        while (leave != 'y' and leave != 'n'):
            
            
            print(scissors)
            print("YOU: scissors")
            
            print(paper)
            print("COMPUTER: paper")

            print('\n')
            print(win)
            print('\n\nYou chose scissors, computer chose paper.')
            print("You win! Play again? y/n")
            leave = input()
            if leave != 'y' and leave != 'n':
                print("Please enter a valid choice.")
            if leave == 'n':
                print("Goodbye.")
                exit()
            elif leave == 'y':
                pass

