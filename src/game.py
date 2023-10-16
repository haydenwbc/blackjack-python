import random
from utils import VALUES, SUITS # import value and suit constants from utils.py

def generate_decks(num_decks):
    i = 0
    shoe = [] # represents shoe containing all decks (will usually be 6)
    while i < num_decks:
        deck = [] #Empty List for deck

        #populate deck with cards represented as tuples (value, suit)
        for value in VALUES:
            for suit in SUITS:
                deck.append([value, suit])
        random.shuffle(deck)
        shoe.extend(deck) # all decks in shoe are shuffled together rather than treated as individual decks
        i += 1
    random.shuffle(shoe)  # shoe shuffled again for good measure
    return shoe

def deal_cards(num_players, shoe): #takes a generated shoe as well as a number of players (usually 1 until multiplayer/AI implemented)
    hands = {} # dictionary to represent the hands of the game, dealer entry will include actual hand and display hand with face down card
    i = 0 # iterator for loop
    #generate hands for each player
    while i < num_players:
        player_hand = [shoe.pop(), shoe.pop()]
        hands[f"Player {i+1}"] = player_hand
        i += 1
        
    dealer_hand = [shoe.pop(), shoe.pop()]
    hands["Dealer"] = dealer_hand #create dictionary entry for true dealer hand
    
    return hands #dictionary structure as follows {Player Num}

def print_hands(hands):
    num_players = len(hands) - 1
    i = 0
    while i < num_players:
        print(f"Hand of Player {i +1}:")
        print(f"{hands[f'Player {i+1}'][0][0]} of {hands[f'Player {i+1}'][0][1]}s") #Print first card
        print(f"{hands[f'Player {i+1}'][1][0]} of {hands[f'Player {i+1}'][1][1]}s") #Print second card

    







