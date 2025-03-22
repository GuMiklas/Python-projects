import random
print("\n" + "*" * 140)
print("\nThis is a number guessing game. The game will pick a random number between 1 and 100 and you have to guess it within 5 guesses. Good luck!\n")
print("*" * 140)
number_to_guess = random.randint(1,100)
guesses = 0
total_guesses = 5
while guesses <= 5:
    guess = input("Guess a number between 1 and 100: ")
    if int(guess) == number_to_guess:
        print("You guessed the number in " + str(guesses) + " guesses!")
        print("The number was " + str(number_to_guess))
        break
    elif int(guess) > number_to_guess:
        print("\tYour guess is too high!")
        guesses = guesses + 1
        total_guesses = total_guesses - 1
    elif int(guess) < number_to_guess:
        print("\tYour guess is too low!")
        total_guesses = total_guesses - 1
        guesses = guesses + 1
    if int(guesses) == 5:
        print("\tSorry, you ran out of guesses!, the number was " + str(number_to_guess))
        break
    print("\tYou have " + str(total_guesses) + " guesses left!\n")
