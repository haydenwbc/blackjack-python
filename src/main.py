import game

NUM_PLAYERS = 3
NUM_DECKS = 6

shoe = game.generate_decks(NUM_DECKS)

hands = game.deal_cards(NUM_PLAYERS, shoe)

game.print_hands(hands)

