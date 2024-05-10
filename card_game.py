import random

# Define a class to represent the players
class Players:
    def __init__(self, name_one, name_two):
        # Initialize the players with their names
        self.name_one = name_one
        self.name_two = name_two
        # Reset the win counts for both players
        self.reset_wins()

    # Method to reset the win counts for both players
    def reset_wins(self):
        self.wins = {self.name_one: 0, self.name_two: 0}

# Define a class to represent the deck of cards
class Deck:
    def __init__(self):
        # Initialize the deck
        self.create_deck()

    # Method to create a standard deck of cards
    def create_deck(self):
        self.cards = []
        # Define ranks and suits for the cards
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        # Define values for each rank and ranks for each suit
        self.rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.suit_ranks = {'Clubs': 1, 'Diamonds': 2, 'Hearts': 3, 'Spades': 4}
        # Create each card and add it to the deck
        for rank in self.ranks:
            for suit in self.suits:
                self.cards.append([rank, suit])
        # Shuffle the deck
        self.shuffle_deck()

    # Method to shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.cards)

    # Method to deal two cards from the deck
    def deal_cards(self):
        card1 = self.cards.pop()
        card2 = self.cards.pop()
        return card1, card2

    # Method to determine the winner between two cards
    def winner(self, card1, card2, players):
        rank_card1, suit_card1 = card1
        rank_card2, suit_card2 = card2

        # Compare ranks of the cards
        if self.rank_values[rank_card1] > self.rank_values[rank_card2]:
            winner = players.name_one
        elif self.rank_values[rank_card2] > self.rank_values[rank_card1]:
            winner = players.name_two
        else:
            # If ranks are equal, compare suits
            if self.suit_ranks[suit_card1] > self.suit_ranks[suit_card2]:
                winner = players.name_one
            else:
                winner = players.name_two
        
        # Update the win count for the winner
        players.wins[winner] += 1

        return winner


# Get player's names from user input
name_one = input(f'Player one name: ')
name_two = input(f'Player two name: ')
# Create players with the provided names
players = Players(name_one, name_two)
# Create a deck of cards
deck = Deck()

# Main game loop
while True:
    # Create a new deck and shuffle it
    deck.create_deck()
    deck.shuffle_deck()
    # Deal two cards from the deck
    card1, card2 = deck.deal_cards()

    # Display the cards of each player
    print(f"{name_one}'s card is: {card1}")
    print(f"{name_two}'s card is: {card2}")

    # Determine the winner of the round
    winner = deck.winner(card1, card2, players)
    print(f'{winner} wins!')

    # Display the updated win counts for both players
    print(f'{players.name_one} wins: {players.wins[players.name_one]}')
    print(f'{players.name_two} wins: {players.wins[players.name_two]}')

    # Ask the players if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break







# def test_tie():
#     test_card = ['5', 'Hearts']
#     test_card2 = ['5', 'Spades']
#     assert rank_values[test_card[0]] == rank_values[test_card2[0]]
#     # assert rank_values[2] == rank_values[


# test_tie()




        


