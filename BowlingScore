# File: Bowling.py
# Description: Program that calculates bowler's average and handicap 
# Assignment Number: 3
#
# Name: Alicia Ireland
# EID:  ani324
# Email: alicianireland@gmail.com
# Grader: Noah
# Slip days used this assignment: 0
#
# On my honor, Alicia Ireland, this programming assignment is my own work
# and I have not provided this code to any other student.


# Calculate bowlers average and handicap using scores from 3 games.
def main():
    # Get bowler's name.
    name = input("Enter your name: ")
    print()
    # Get bowler's score for three games played.
    game_one_score = int(input("Enter Game 1: "))
    game_two_score = int(input("Enter Game 2: "))
    game_three_score = int(input("Enter Game 3: "))
    print()
    # Calculate and print out bowler's average and handicap.
    average_score = (game_one_score + game_two_score
                     + game_three_score) // 3
    handicap = int(((200 - average_score) * .8) // 1)
    
    print(name + "'s average is:", average_score)
    print(name + "'s handicap is:", handicap)


main()
