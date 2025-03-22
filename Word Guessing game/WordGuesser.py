import random

word_list = ['tractor', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'cybersecurity',
         'reverse', 'nerd', 'table', 'geeks', 'taltech']

word = random.choice(word_list)
print("\n" + "*" * 53)
print("\nIn this game, you have to guess the word, good luck!\n")
print("*" * 53)
print("Guess the characters! You have 10 guesses!")

guesses = ''
turns = 10


while turns > 0: #Loop for the game

    unsolved = 0

    for char in word: # Iterate through word, print char if it exists or _ if it doesn't

         if char in guesses:
                print(char)
         else:
                print("_")
                unsolved = 1

    if unsolved == 0: # If no spaces are unsolved, win

        print("\nYou guessed the word!\n")
        print("The word was: " + word)
        break

    guess = input("\nGuess a character: ")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("\nWrong")
        print("You have " + str(turns) + " guesses remaining.\n")

    if turns == 0:

        print("You Lose! The word was: " + word)