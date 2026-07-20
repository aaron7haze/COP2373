# deck.py
# Deck class for a standard 52-card deck

import random

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8",
                 "9", "10", "Jack", "Queen", "King"]

        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(f"{rank} of {suit}")

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        # Remove and return the top card
        return self.cards.pop()
