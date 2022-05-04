# File: Dice.py
# Description: A  program that simulates the casino dice game, Craps.
# Assignment Number: 6 
#
# Name: Alicia Ireland
# EID:  ani324
# Email: alicianireland@gmail.com
# Grader: Noah
#
# On my honor, Alicia Ireland, this programming assignment is my own work
# and I have not provided this code to any other student.
import random


# Get the number of rounds from the user and seed value, if wanted,
# to simulate a game of Craps and determine both, the number
# of rounds the user won and the max number of rolls in the game.
def main():
    print("This program simulates the dice game of craps.")
    # Ask user they want to set the seed
    want_set_seed = input("Do you want to set the seed? Enter y for yes, "
                          + "anything else for no: ")

    # Set seed to value input by user or dont call seed .
    if want_set_seed == "y":
        int_seed = int(input("Enter an int for the initial seed: "))
        random.seed(int_seed)
    #else:
        #call_seed = 0

    # Ask user for number of rounds to play.
    NUMBER_OF_ROUNDS_TOTAL = int(input("Enter the number of rounds to"
                                       +" run: "))
    
    number_of_rounds = 0
    times_won = 0 
    max_rolls_in_a_round = 0
    #call_seed
    
    # Loop to simulate one round of craps at a time and continue
    # to loop until  desired number of rounds is reached.
    # Keeps track of number of rounds, total times won and
    # the maximum number of rolls.
    while number_of_rounds < NUMBER_OF_ROUNDS_TOTAL:
        number_of_rounds += 1

        # Roll two dice to get initial roll value
        side_of_first_dice = random.randint(1,6)
        side_of_second_dice = random.randint(1,6)
        initial_roll = side_of_first_dice + side_of_second_dice

        # Determine if user won, lost, or should roll again
        if initial_roll == 7 or initial_roll == 11:
            times_won += 1
            total_rolls_this_round = 1   
        elif initial_roll == 2 or initial_roll == 3 or initial_roll == 12:
            total_rolls_this_round = 1
        else:
            total_rolls_this_round = 1
            point = initial_roll
            next_roll = 0
            # Continue rolling dice until player looses or wins
            while next_roll != 7 and next_roll != point:
                total_rolls_this_round += 1
                side_of_first_dice = random.randint(1,6)
                side_of_second_dice = random.randint(1,6)
                next_roll = side_of_first_dice + side_of_second_dice
                    
            if next_roll == point:
                times_won += 1
               
        # Determine maximum number of rolls after round is over.
        if total_rolls_this_round > max_rolls_in_a_round:
            max_rolls_in_a_round = total_rolls_this_round
            
    # Print number of times won and the maximum number of rolls.     
    if NUMBER_OF_ROUNDS_TOTAL < 0:
         print("Player won", times_won, "times in 0 rounds.")
    else:
        print("Player won", times_won, "times in", NUMBER_OF_ROUNDS_TOTAL, \
              "rounds.")

    print("Maximum number of rolls in a round =", max_rolls_in_a_round)

 
main()
