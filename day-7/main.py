import hangman_art as art
import hangman_words as words
import random

def pass_error_check(guess, guesses):
    if (len(guess) > 1):
        print('Please enter just one letter')
        return False

    if (not guess.isalpha()):
        print('Please only enter letters')
        return False

    if (guess in guesses):
        print('\nYou already guessed that letter!')
        print()
        print('Guesses: ', end ='')
        print(*guesses)
        return False
    
    return True

logo = art.logo
stages = art.stages
word_list = words.word_list

random_word = random.randint(0, len(word_list))
word = word_list[random_word]
print(word)
spaces = []
guesses = []
guessed = False
game_end = False
lives = 6
correct = False

for space in word:
    spaces += '_'

print(logo)

while(not game_end):

    print(stages[lives])
    print(*spaces)

    guess = input('\nGuess a letter: ').lower()

    if guess == '?':
        print(f'Guesses: {guesses}')

    while(not pass_error_check(guess, guesses)):
        if guess == '?':
            print(f'Guesses: {guesses}')
        guess = input('\nGuess a letter: ').lower()

    for i in range(len(word)):

        if (guess == word[i]):
            correct = True
            guessed = True
            spaces[i] = word[i]
    
    if correct:
        print('\nCorrect!')
    
    guesses += guess

    if (guessed is False):
        print('\nWrong!')
        lives -= 1
    guessed = False

    if lives is 0:
        print('\nYou lose!\n')
        print(f'Word was {word}\n')
        game_end = True

    if '_' not in spaces:
        print('You Win!')
        game_end = True

    correct = False