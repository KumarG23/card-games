# PseudoCode

## start

Will need 4 suits - spades, clubs, hearts, diamonds. in a list []
Will need each card number in a list of ranks. ranks = ['A', '2', etc.] 
will need to have an empty list for cards. cards[]
we will populate the cards list with a for loop with cards.append

for suit in suites:
    for rank in ranks:
        cards.append([suit, rank])

print(cards)

using the random function that we can import into python we can shuffle the cards. 

for the actual game we need to return 2 cards and have the high card win. 