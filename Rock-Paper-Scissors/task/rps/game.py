import random

choose = input()
option = ["scissors", "paper", "rock"]
computerChoice = random.choice(option)
if (choose == "scissors"):
    if computerChoice == "scissors":
        print(f'There is a draw ({computerChoice})')
    elif computerChoice == "paper":
        print(f'Well done. The computer chose {computerChoice} and failed')
    else:
        print(f'Sorry, but the computer chose {computerChoice}')
elif (choose == "paper"):
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