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
    
    #Print Player hands
    while i < num_players:
        print(f"Hand of Player {i +1}:")
        for index, card in enumerate(hands[f"Player {i+1}"]):
            print(f"{index+1}. {card[0]} of {card[1]}")
        i += 1
        print()
            
    print("Dealer Hand:")
    for index, card in enumerate(hands["Dealer"]):
        if (index+1) == 2:
            print(f"{index + 1}. Face Down Card")
        else:
            print(f"{index+1}. {card[0]} of {card[1]}")
            
def print_player_hand(player, hands):
    print(f"{player}'s Hand:")
    for index, card in enumerate(hands[player]):
        print(f"{index+1}. {card[0]} of {card[1]}")
        i += 1

            
def init_bank(num_players):
    bank = {}
    i = 0
    while i < num_players:
        bank[f"Player {i+1}"] = 1000
        i += 1
        
    return bank

def place_bet(bank, player):
    bet_amt = input(f"{player}, place a bet between $1 and ${bank[player]}: ")
    bank[player] -= bet_amt
    
    return bank 

def play_turn(shoe, bank): 
    
    hands = deal_cards(len(bank.keys()), shoe)
    
    for player in bank.keys():
        
        print(f"{player}'s turn:")
        place_bet(bank, player)
    
        
        while True:
            print_player_hand(player, hands)
            action = input("Do you want to hit or stand? ").lower()
            if action == "hit":
                hands[player].append(shoe.pop())
                print(f"You drew a {hands[player][-1][0]} of {hands[player][-1][1]}")




