# AaronHaze_ProgrammingExercise11.py
# Programming Exercise 11 - Poker Hand Draw
# Author: Aaron Haze

from deck import Deck   # Import Deck class from deck.py

# ----- Function: deal_hand -----
# Deals a 5-card poker hand from the deck
def deal_hand(deck):
    hand = []
    for _ in range(5):
        hand.append(deck.draw())
    return hand

# ----- Function: replace_cards -----
# Replaces selected cards (1–5) with new ones from the deck
def replace_cards(hand, deck, selections):
    for index in selections:
        # Convert human input (1–5) to zero-based index
        hand[index - 1] = deck.draw()
    return hand

# ----- MAIN PROGRAM -----
def main():
    deck = Deck()
    deck.shuffle()

    print("Your initial poker hand:")
    hand = deal_hand(deck)
    print(hand)

    # Ask user which cards to replace
    user_input = input("Enter card numbers to replace (example: 1 3 5): ")

    if user_input.strip() == "":
        selections = []
    else:
        selections = [int(num) for num in user_input.split()]

    # Replace selected cards
    new_hand = replace_cards(hand, deck, selections)

    print("\nYour final hand after the draw:")
    print(new_hand)

# Run the program
if __name__ == "__main__":
    main()
