import random

userName = ...
score = 0


def choosingUser():
    global userName

    userName = input("Enter your name: ")
    print("Hello,", userName)


def checkRating():
    global userName
    global score

    file = open("rating.txt", mode="r")
    for line in file:
        if userName in line:
            stripped = line.split()
            score = int(stripped[1])
    file.close()


def choosingOption():
    options = ['rock', 'paper', 'scissors', '!rating', '!exit']
    optionChoose = input()
    while optionChoose not in options:
        print("Invalid input")
        optionChoose = input()
    return optionChoose


def gameLogic(userChoice):
    global score
    options = ['rock', 'paper', 'scissors']
    computerChoice = random.choice(options)
    if userChoice == "scissors":
        if computerChoice == "scissors":
            print(f'There is a draw ({computerChoice})')
            score += 50
        elif computerChoice == "paper":
            print(f'Well done. The computer chose {computerChoice} and failed')
            score += 100
        else:
            print(f'Sorry, but the computer chose {computerChoice}')
    elif userChoice == "paper":
        if computerChoice == "scissors":
            print(f'Sorry, but the computer chose {computerChoice}')
        elif computerChoice == "paper":
            print(f'There is a draw ({computerChoice})')
            score += 50
        else:
            print(f'Well done. The computer chose {computerChoice} and failed')
            score += 100
    else:
        if computerChoice == "scissors":
            print(f'Well done. The computer chose {computerChoice} and failed')
            score += 100
        elif computerChoice == "paper":
            print(f'Sorry, but the computer chose {computerChoice}')
        else:
            print(f'There is a draw ({computerChoice})')
            score += 50


def playGame():
    global userName
    global score

    userChoice = choosingOption()
    while userChoice != "!exit":
        if userChoice == "!rating":
            print("Your rating:", score)
            userChoice = choosingOption()
        else:
            gameLogic(userChoice)
            userChoice = choosingOption()
    print("Bye!")


choosingUser()
checkRating()
playGame()
