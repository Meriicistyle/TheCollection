import random
import sys

element = ["rock","paper","scissors"]

while True:
    
    print("""        
        --> Welcome to the rock, paper
            scissors game. Enter your
            choice and play against
            "The SCripT"!
        """)

    computerchoice = random.choice(element)

    player = str.lower(input("Rock, paper or scissors: "))

    if computerchoice == "rock":
        if player == "paper":
            print("""
            -- You won! The SCripT chose rock! --""")
            continue
        elif player == "scissors":
            print("""
            -- The SCripT won and chose rock :'( --""")
            continue
        elif player == "rock":
            print("""
            -- It's a tie! --""")
            continue

    if computerchoice == "paper":
        if player == "rock":
            print("""
            -- The SCripT won and chose paper :'( --""")
            continue
        elif player == "scissors":
            print("""
            -- You won! The SCripT chose paper! --""")
            continue
        elif player == "paper":
            print("""
            -- It's a tie! --""")
            continue

    if computerchoice == "scissors":
        if player == "rock":
            print("""
            -- You won! The SCripT chose scissors! --""")
            continue
        elif player == "paper":
            print("""
            -- The SCripT won and chose scissors :'( --""")
            continue
        elif player == "scissors":
            print("""
            -- It's a tie! --""")
            continue