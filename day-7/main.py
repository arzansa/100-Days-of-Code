import random


word_list = ["aardvark", "baboon", "camel"]


random_word = random.randint(0, 2)
word = word_list[random_word]
print(word)
spaces = []
guessed = False
game_end = False
times_wrong = 0

for space in word:
    spaces += '_'

while(not game_end):

    print(spaces)
    guess = input('Guess a letter: ').lower()

    for i in range(len(word)):
        if (guess == word[i]):
            guessed = True
            spaces[i] = word[i]

    if (guessed is False):
        print('Wrong!')
        times_wrong += 1
    guessed = False

    if times_wrong is 6:
        print('You lose!')
        game_end = True

    if '_' not in spaces:
        print('You Win!')
        game_end = True