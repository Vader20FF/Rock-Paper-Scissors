import random

userName = ...
score = 0
userOptionsChose = []


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


def choosingAllOptions():
    global userOptionsChose
    optionsString = input()
    if len(optionsString) == 0:
        userOptionsChose = ['rock', 'paper', 'scissors']
    else:
        userOptionsChose = optionsString.split(",")
    print("Okay, let's start")
    userOptionsChose.append("!rating")
    userOptionsChose.append("!exit")


def choosingOption():
    global userOptionsChose

    optionChose = input()
    while optionChose not in userOptionsChose:
        print("Invalid input")
        optionChose = input()
    return optionChose


def gameLogic(userChoice):
    global score
    global userOptionsChose

    winning_cases = {
        'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
        'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
        'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
        'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
        'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
        'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
        'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
        'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
        'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
        'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
        'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
        'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
        'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
        'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
        'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
    }

    computerOptionsChose = userOptionsChose[0:-2]
    computerChoice = random.choice(computerOptionsChose)
    if userChoice == computerChoice:
        print(f'There is a draw ({computerChoice})')
        score += 50
    else:
        if userChoice in winning_cases[computerChoice]:
            print(f'Sorry, but the computer chose {computerChoice}')
        else:
            print(f'Well done. The computer chose {computerChoice} and failed')
            score += 100


def playGame():
    global userName
    global score
    global userOptionsChose

    choosingAllOptions()
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
