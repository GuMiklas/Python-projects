import random
print("\n" + "*" * 40)
print("\nThis is a game of rock, paper, scissors.\n")
print("*" * 40)
choice_USER = int(input("Make a choice: \n1. Rock\n2. Paper\n3. Scissors\n"))
choice_BOT = random.randint(1, 3)

# 1 = rock, 2 = paper, 3 = scissors

if  choice_BOT == choice_USER:
    print("It's a tie!\n You both chose the same item!")
elif choice_BOT == 1 and choice_USER == 2:
    print("You win!\n The BOT chose ROCK and you chose PAPER")
elif choice_BOT == 1 and choice_USER == 3:
    print("You lose!\n The BOT chose ROCK and you chose SCISSORS")
elif choice_BOT == 2 and choice_USER == 1:
    print("You lose!\n The BOT chose PAPER and you chose ROCK")
elif choice_BOT == 2 and choice_USER == 3:
    print("You win!\n The BOT chose PAPER and you chose SCISSORS")
elif choice_BOT == 3 and choice_USER == 1:
    print("You win!\n The BOT chose SCISSORS and you chose ROCK")
elif choice_BOT == 3 and choice_USER == 2:
    print("You lose!\n The BOT chose SCISSORS and you chose PAPER")
