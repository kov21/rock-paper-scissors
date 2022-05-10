#rock paper scissors

import random
rps = ["rock", "paper", "scissors"]
option = input ("Hello and welcome to my rock paper scissors game! Press y to play or n to quit")

while option == "y":
    x = random.randint (0,2)
    pChoice = input("Choose between rock paper and scissors")

    if pChoice == "rock":
        if rps[x] == "rock":
            print ("The computer chose rock, this game is a tie")
        elif rps[x]== "paper":
            print ("The computer chose paper, you lose")
        elif rps[x] == "scissors":
            print ("The computer chose scissors, you win")

    elif pChoice == "paper":
        if rps[x] == "rock":
            print ("The computer chose rock, you win")
        elif rps[x] == "paper":
            print ("The computer chose paper, this game is a tie")
        elif rps[x] == "scissors":
            print ("The computer chose scissors, you lose")

    elif pChoice == "scissors":
        if rps[x] == "rock":
            print ("The computer chose rock, you lose")
        elif rps[x] == "paper":
            print ("The computer chose paper, you win")
        elif rps[x] == "scissors":
            print ("The computer chose scissors, this game is a tie")
    
    option = input ("Replay, y/n")
