import random

userInput = input()
options = ["scissors", "paper", "rock"]
while userInput != "!exit":
    while userInput not in options:
        if userInput == "!exit":
            break
        print("Invalid input")
        userInput = input()
    if userInput == "!exit":
        break
    computerChoice = random.choice(options)
    if userInput == "scissors":
        if computerChoice == "scissors":
            print(f'There is a draw ({computerChoice})')
        elif computerChoice == "paper":
            print(f'Well done. The computer chose {computerChoice} and failed')
        else:
            print(f'Sorry, but the computer chose {computerChoice}')
    elif userInput == "paper":
        if computerChoice == "scissors":
            print(f'Sorry, but the computer chose {computerChoice}')
        elif computerChoice == "paper":
            print(f'There is a draw ({computerChoice})')
        else:
            print(f'Well done. The computer chose {computerChoice} and failed')
    else:
        if computerChoice == "scissors":
            print(f'Well done. The computer chose {computerChoice} and failed')
        elif computerChoice == "paper":
            print(f'Sorry, but the computer chose {computerChoice}')
        else:
            print(f'There is a draw ({computerChoice})')
    userInput = input()

print("Bye!")
