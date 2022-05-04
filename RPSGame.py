# File: RPS.py
# Description: A program that simulates the Rock, Paper, Scissors game.
# Assignment Number: 7
#
# Name: Alicia Ireland
# EID:  ani324
# Email: alicianireland@gmail.com
# Grader: Noah
#
# On my honor, Alicia Ireland, this programming assignment is my own work
# and I have not provided this code to any other student.
import random


# Get users input to simulate round of Rock, Paper, Scissors game
# for user chosen number of rounds and call functions to determine winner
def main():
    print("Welcome to ROCK PAPER SCISSORS. I, Computer," +
          " will be your opponent.")

    name = input_statements("Please enter your name: ")
    num_rounds = int(input_statements
                     ("Please enter the number of rounds to play: "))
    want_set_seed = (input_statements
                     ("Please enter y if you want to set the seed: "))
    #Set seed if user said yes
    if  want_set_seed == "y":
        set_seed = int(input_statements
                       ("Please enter an integer for the seed: "))
        random.seed(set_seed) 
        
    tot_win = 0
    # Loop that simulates each round of RPS and calls other functions 
    for i in range (1, num_rounds + 1):
        print("**** Round", i, "****")
        print(name + "," + " enter your choice for this round.")
        user_choice = input("R for Rock, P for Paper, S for Scissors: ")
        
        computer_choice = random.randint(1,3)
        computer_letter = computer_turn(computer_choice)
        who_won_round = find_who_wins(computer_letter, user_choice)
        user_won = num_wins(who_won_round)
        
        tot_win += user_won
        print()
        
    ouput_statements(name, num_rounds, tot_win)


# Get input values and print out with following details.
def input_statements(question_asked):
    print("***** INITIAL INPUT *****")
    response = input(question_asked)
    print("Thank you!" + "\n")
    
    return response

    
# Turn computers numerical value to letter form     
def computer_turn(comp_num):
    if comp_num == 1:
        print("I pick Rock.")
        comp_lett = "R"
    elif comp_num == 2:
        print("I pick Paper.")
        comp_lett = "P"
    else:
        print("I pick Scissors.")
        comp_lett = "S"

    return comp_lett


# Compare users choice to computers choice to see who wins   
def find_who_wins(comp_letter, user_letter):         
    if comp_letter == user_letter:
        statement = "We picked the same thing."
        who_won = " Round is a draw." 
    elif ((comp_letter == "R" and user_letter == "P") or
          (comp_letter == "P" and user_letter == "R")):
        statement = "Paper covers Rock. "
        if comp_letter == "P":
            who_won = "I win."
        else:
            who_won = "You win."
    elif ((comp_letter == "R" and user_letter == "S") or
          (comp_letter == "S" and user_letter == "R")):
        statement = "Rock breaks Scissors. "
        if comp_letter == "R":
            who_won = "I win."
        else:
            who_won = "You win."
    else:
        statement = "Scissors cut Paper. "
        if comp_letter == "S":
            who_won = "I win."
        else:
            who_won = "You win."   
    print(statement + who_won)
    return who_won
        

# Keeps track of number of time user wins
def num_wins(win_or_not):
    if win_or_not == "You win.":
        win_or_not = 1
    else:
        win_or_not = 0
    return win_or_not


# Print output statments depending of number of rounds played and won
def ouput_statements(name,total_rounds, total_wins):
    if total_rounds == 1:
        print("We played", total_rounds, "round of ROCK PAPER SCISSORS.")
    else:
        print("We played", total_rounds, "rounds of ROCK PAPER SCISSORS.")
        
    if total_wins ==1:
        print(name, "won", total_wins, "round.")
    else:
        print(name, "won", total_wins, "rounds.")

    print("Well played.")


main()
