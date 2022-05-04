# File: racko.py
# Description: A program that simulates the card and number game
# Rack-O. Players use the keyboard and take turns.
# Assignment Number: 10
#
# Name: Alicia Ireland
# EID:  ani324
# Email: alicianireland@gmail.com
# Grader: Noah
#
#Â On my honor, Alicia Ireland, this programming assignment is my own work
#Â and I have not provided this code to any other student. 

import random


# Play one game of Rack-O.
def main():
    # Get the rack size, create the deck, and deal the initial racks.
    rack_size = prep_game()
    deck = list(range(1, 61))
    random.shuffle(deck)
    player = 1
    player_1_rack = get_rack(deck, rack_size)
    player_2_rack = get_rack(deck, rack_size)
    discard = [deck.pop(0)] 
    player_rack = player_1_rack
    
   # Simulates each round, switching between each player's turn, until
   # either player 1's or player 2's rack is sorted in ascending order 
    while (is_sorted(player_rack) != True):
        if player % 2 != 0:
            player_rack = player_1_rack
            print("Player 1's turn.")
        else:
            player_rack = player_2_rack
            print("Player 2's turn.")
        player = move_made(player_rack, deck, discard, player)
            
    print("Player 1 wins!") if player % 2 == 0 else print("Player 2 wins!")
     
        
# Get ready to play 1 game.
# Show the instructions if the user wants to see them.
# Set the seed for the random number generator.
# Return the size of the rack to use.
def prep_game():
    print('----- Welcome to Rack - O! -----')
    if input('Enter y to display instructions: ') == 'y':
        instructions()
    print()
    random.seed(eval(input('Enter number for initial seed: ')))
    rack_size = eval(input('Enter the size of the rack to use. '
                            + 'Must be between 5 and 10: '))
    while not 5 <= rack_size <= 10:
        print(rack_size, 'is not a valid rack size.')
        rack_size = eval(input('Enter the size of the rack to use. '
                            + 'Must be between 5 and 10: '))
    print()
    return rack_size


# Print the instructions of the game.
def instructions():
    print()
    print('The goal of the game is to get the cards in your rack of cards')
    print('into ascending order. Your rack has ten slots numbered 1 to 10.')
    print('During your turn you can draw the top card of the deck or take')
    print('the top card of the discard pile.')
    print('If you draw the top card of the deck, you can use that card to')
    print('replace a card in one slot of your rack. The replaced card goes to')
    print('the discard pile.')
    print('Alternatively you can simply choose to discard the drawn card.')
    print('If you take the top card of the discard pile you must use it to')
    print('replace a card in one slot of your rack. The replaced card goes')
    print('to the top of the discard pile.')


# Take the player's turn. Give them the choice of drawing or taking
# the top card of the discard pile. If they draw they can replace
# a card or discard the draw. If they take the top card of the discard
# pile they must replace a card in their rack.
def take_turn(deck, discard, player_rack):    
    print("Your current rack ", player_rack)    
    print("Top of discard pile ", discard[0])    
    choice = input("Enter d to draw anything else to take top of" +\
                   " discard pile: ")
    print()
    
    if choice == "d":
        new_card = deck.pop(0)
        print("drew the", new_card)
        choice = input("Enter p to place card, anything else to discard it: ")
        if choice != "p":
            discard.insert(0, new_card)
            new_card = 0        
    else:
        new_card = discard[0]
        
    return new_card


# Determines whether to place card and then move on to
# next players turn or to just move onto next players turn
# based on if player can discard card or not. After players turn,
# makes sure deck is not empty.
def move_made(player_rack, deck, discard, player):
    new_card = take_turn(deck, discard, player_rack)
    if new_card == 0:
        print("The rack after the turn ", player_rack)
        print()
        player += 1
    else:
        place_card(player_rack, new_card, discard)
        print("The rack after the turn ", player_rack)
        print()
        player += 1

    if len(deck) == 0:
        print("Deck is empty. Shuffling discard pile.")
        make_new_deck(deck, discard)
        
    return player
   

# Ask the player which card to replace in their rack.
# Replace it with the given new card. Place the card removed
# from the player's rack at the top of the discard pile.
# Error checks until player enters a card that is currently
# in their rack.
def place_card(player_rack, new_card, discard):
    card_to_replace = int(input("Enter the card number to replace with " + \
                                "the " + str(new_card) + ": " ))
    while card_to_replace not in player_rack:
        print(card_to_replace, "is not in your rack.")
        card_to_replace = int(input("Enter the card number to replace " + \
                                "with the " + str(new_card) + ": " ))
        
    index_of_card = player_rack.index(card_to_replace)
    player_rack.pop(index_of_card)
    player_rack.insert(index_of_card, new_card)
    discard.insert(0, card_to_replace)
       
           
# Return True if this rack is sorted in ascending order, False otherwise.
# Do not create any new lists in this function.
def is_sorted(rack):
    in_order = True
    i= 0
    while in_order and i < len(rack)-1:
        if rack[i] > rack [i+1]:
            in_order = False
        else:
            i += 1
    return in_order   


# Deal the top 10 cards of the deck into a new rack. The first
# card goes in the first slot, the second card goes in the second
# slot, and so forth. We assume len(deck) >= rack_size. Return the
# list of ints representing the rack.
def get_rack(deck, rack_size):
    rack = []
    while len(rack) < rack_size:
        rack += [deck[0]]
        deck.pop(0)
    return rack


# Makes new deck if all cards are drawn from deck. Discard pile
# is shuffled and becomes new deck and card at top of new deck
# get flipped and becomes new discard pile.
def make_new_deck(deck, discard):
    random.shuffle(discard)
    i = 0
    while len(discard) != 0:
        card = discard.pop(0)
        deck.insert(i, card)
        i += 1
    discard.insert(0, deck.pop(0))

    
main()
