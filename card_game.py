import random


# class Players:
#     def __init__(self, name_one, name_two):
name_one = (input(f'Player one name: '))
name_two = (input(f'Player two name: '))
        # self.name_one = (input(f'Player one name: '))
        # self.name_two = (input(f'Player two name: '))

    
# class Deck:
#     def __init__ (self, cards, ranks, suits)
#         self.cards = []
#         self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#         self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
cards = []
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# ranks = ['2']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


#append suit and rank into the card list
for rank in ranks:
    for suit in suits:
        cards.append([rank, suit])


random.shuffle(cards)

card = cards.pop()
card2 = cards.pop()


print(f"{name_one}'s card is: {card}")
print(f"{name_two}'s card is: {card2}")

rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suit_ranks = {'Clubs': 1, 'Diamonds': 2, 'Hearts': 3, 'Spades': 4}


if rank_values[card[0]] > rank_values[card2[0]]:
    print(f'{name_one} wins!')
elif rank_values[card2[0]] > rank_values[card[0]]:
    print(f'{name_two} wins!')
else:
    if suit_ranks[card[1]] > suit_ranks[card2[1]]:
        print(f'{name_one} wins!')
    elif suit_ranks[card2[1]] > suit_ranks[card[1]]:
        print(f'{name_two} wins!')




def test_tie():
    test_card = ['5', 'Hearts']
    test_card2 = ['5', 'Spades']
    assert rank_values[test_card[0]] == rank_values[test_card2[0]]
    # assert rank_values[2] == rank_values[


test_tie()




        


