#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: March 10 2020
# This program is a rock paper scissors game

from random import randint

#create a list of play options
print("Rock, Paper, Scissors Game. Please Pick a Move.")
game = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = game[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors: ")
    if player == computer:
        print("Game is a Tie!")
        break
    elif player == "Rock":
        if computer == "Paper":
            print("Computer Win,", "You lose!", computer, "covers", player)
            break
        else:
            print("You win!,", "Computer lose!", player, "smashes", computer)
            break
    elif player == "Rock":
        if computer == "Scissors":
            print("You Win!,", "Computer lose!", computer, "covers", player)
            break
        else:
            print("You win!,", "Computer lose!", player, "smashes", computer)
            break
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer Win,", "You lose!", computer, "cut", player)
            break
        else:
            print("You win!,", "Computer lose!", player, "covers", computer)
            break
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer Win,","You lose!", computer, "smashes", player)
            break
        else:
            print("You win!,", "Computer Lose!", player, "cut", computer)
            break
    else:
        print("That's not a valid Input. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = game[randint(0,2)]