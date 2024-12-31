"""Simulating and attempting to find best 31 card game strategy"""


import random
from typing import Union

# defining a deck of cards w/o jokers
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
deck = [(value, suit) for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] for suit in suits]


# player has a specified strategy and 3 initial quarters which count as lives
class Player:
    quarters: int
    wins: int
    hand: list[Union[int, str]]
    points: int
    strategy: str

    def __init__(self, strategy: str):
        self.quarters = 3
        self.wins = 0
        self.hand = []
        self.points = 0
        self.strategy = strategy
    
    def __str__(self):
        return self.strategy

    def sum_points(self):
        # Check if all cards have the same suit
        if len(set(card[1] for card in self.hand)) == 1:  # Check unique suits
            total = 0
            for card in self.hand:
                value = card[0]
                if value in ["Jack", "Queen", "King"]:
                    total += 10
                elif value == "Ace":
                    total += 11
                else:
                    total += value
            return total
        return 0  # if suits don't match, score is 0

    
    def has31(self):
        return self.sum_points() == 31


def deal_cards(players: list[Player], deck):
    shuffled_deck = deck[:]
    random.shuffle(shuffled_deck)
    for player in players:
        player.hand = shuffled_deck[:3]  # each card is a tuple (value, suit)
        del shuffled_deck[:3]
    return shuffled_deck

def game(players, deck):
    #initialize players
    player_list = [Player() for _ in range(players)]
    for player in player_list:
        player.quarters = 3
        player.hand = []
    #initialize players' cards
    #returns a shuffled deck w/o cards in players hands
    shuffled_deck = deal_cards(player_list, deck) 

    #top cards, the ones the players can see
    active_cards = []
    #randomly picking and removing card
    top_card = random.choice(shuffled_deck)
    active_cards.append(top_card)
    shuffled_deck.remove(top_card)
    
    #game loop
    while len(player_list) > 1:
        for player in player_list[:]:
            if player.quarters < 0:
                player_list.remove(player)
            elif player.has31(): 
                # might need to move condition into else block 
                # probably should do this
                # need to check if player has 31 at the end of their turn
                return str(Player)
            else:
                #player's strategy
                #conditionals that check self.strategy
                pass

def knock():
    """knocking game mechanic"""
    #idk if it needs args at the moment

def wait_for_31(player: Player, shuffled_deck, active_cards, top_card):
    """strategy that just waits until points total is 31"""
    if player.sum_points == 31:
        return str(player)
    else:
        #logic for which pile to pick card from
        pass

def knock_at_high_value(player: Player, shuffled_deck, active_cards, top_card):
    """waits until points total is 25, then knocks"""

def indecisive_knock(player: Player, shuffled_deck, active_cards, top_card):
    """has a chance of knocking at certain point totals"""

def knock_first(player: Player, shuffled_deck, active_cards, top_card):
    """knocks on their first turn, simulate with and w/o"""


def game_loop(num, players, deck):
    """loop for game simulation, storing result to dict"""
    result = {}
    for _ in range(num):
        game(players = players, deck = deck)
    
