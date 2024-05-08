import random

name_one = (input(f'Player one name: '))
name_two = (input(f'Player two name: '))

cards = []
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


#append suit and rank into the card list
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])


random.shuffle(cards)

card = cards.pop()
card2 = cards.pop()


print(f"{name_one}'s card is: {card}")
print(f"{name_two}'s card is: {card2}")
