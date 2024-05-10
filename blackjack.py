import random 



class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        #__str__ method returns a string representation of the card in the format 'rank of suit' ex. A of Hearts
    def __str__(self): 
        return (f'{self.rank["rank"]} of {self.suit}')
        

class Deck:
    def __init__(self):
        self.cards = [] # empty list for cards
        ranks = [ # each rank and its value in separate dictionaries stored within a list.
            {'rank': 'A', 'value': 11},
            {'rank': '2', 'value': 2},
            {'rank': '3', 'value': 3},
            {'rank': '4', 'value': 4},
            {'rank': '5', 'value': 5},
            {'rank': '6', 'value': 6},
            {'rank': '7', 'value': 7},
            {'rank': '8', 'value': 8},
            {'rank': '9', 'value': 9},
            {'rank': '10', 'value': 10},
            {'rank': 'J', 'value': 10},
            {'rank': 'Q', 'value': 10},
            {'rank': 'K', 'value': 10},
        ] # list of suits
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

        for rank in ranks: # for loop for rank and suits
            for suit in suits:
                self.cards.append(Card(suit, rank)) # create and add each suit and rank to deck

    def shuffle(self): # shuffle deck method
        random.shuffle(self.cards) # built in random

    def deal(self, number): 
        cards_dealt = [] # list of cards that have been dealt.
        for x in range(number):  # number of cards dealt 
            if len(self.cards) > 0: # ensures there are enough cards to deal
                card = self.cards.pop() # add card from deck.
                cards_dealt.append(card) # add card to cards dealt list.
        return cards_dealt # return cards dealt
    

class Hand:
    def __init__(self, dealer=False):
        self.cards = [] # list of cards for Hand class.
        self.value = 0 # total value of hand
        self.dealer = dealer # indicates dealers hand (boolean)

    def add_card(self, card_list): # add card function
        self.cards.extend(card_list) # add card or cards to hand.

    def calculate_value(self): #calculate value function
        self.value = 0 # value of hand
        has_ace = False # check if hand has an ace. needed for ace to be 1 or 11

        for card in self.cards:
            card_value = int(card.rank['value']) # card value = the card rank number
            self.value += card_value # modify value with current card value
            if card.rank['rank'] == 'A': #check if rank of card is ace. if so change has ace to true
                has_ace = True


        if has_ace and self.value > 21: # if has ace is true and value is > than 21 change self value to be whatever value is - 10. example if cards are A hearts, K hearts and 2 clubs that would be 23 so we want ace to be 1 instead of 11.
            self.value -= 10

    def get_value(self): # get value function
        self.calculate_value() #calc value before returning it
        return self.value
    
    def is_blackjack(self): # is blackjack function
        return self.get_value() == 21
    
    def display(self, show_all_dealer_cards=False): # dont want to show dealer cards until game is over.
        print(f'''{"dealer's" if self.dealer else "your"} hand: ''') # triple quote. pretty cool
        # print dealer's hand if self.dealer is true else print your hand. triple quotes allows single and double quotes in the same line. 

        for index, card in enumerate(self.cards): # use enumerate to keep track of card index in the loop.
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print('hidden')
            else:
                print(card) # hide first card of dealer hand if conditions are met. Print hidden to hide dealers first card. else print the card if not hidden or players hand.

        if not self.dealer:
            print('Value: ', self.get_value())
        print() # if not the the dealer show value of the cards. example hand is A hearts and 5 hearts value is 16. 


class Game:
    def play(self):
        game_number = 0 # keep track of game_number
        games_to_play = 0 # keep track of games to play
        
#while games to play < or = 0 try to have user input how many games they want to play. If they dont enter a number print you must enter a number. Then they can enter a number.
        while games_to_play <= 0:
            try: # similar to try catch.
                games_to_play = int(input(f'How many games do you want to play? '))
            except:
                print('You must enter a number')

        while game_number < games_to_play:
            game_number += 1 # while game number is less than games to play add 1 to game number

            deck = Deck() # shuffle Deck before each game.
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True) # for dealer hand change dealer hand to true.

            for i in range(2): # add two cards to hand (i = placeholder)
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))


            print()
            print('*' * 30) # for decoration
            print(f'{game_number} of {games_to_play}') # what the current game number is of games to play. example game 1 of 3.
            print('*' * 30)
            player_hand.display() # display hands
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand): # check for winner after hands are dealt. possible blackjack.
                continue

            choice = '' # Hit or Stand
            while player_hand.get_value() < 21 and choice not in ['s', 'stand']: # if choice is not s or stand  and value is < 21 give user choice to hit or stand.
                choice = input('Please choose "hit" or "stand" (or H/S): ').lower()
                print() # choose hit or stand.
                while choice not in ['h', 's', 'hit', 'stand']: # choices for input. if choice not recognized in list then tell user to choose hit or stand.
                    choice = input('Please enter either Hit or Stand or (H/S): ').lower()
                    print()
                if choice in ['hit', 'h']: # if hit is chosen then add a card to player hand.
                    player_hand.add_card(deck.deal(1))
                    player_hand.display() 

            if self.check_winner(player_hand, dealer_hand): # check winner again.
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()
            # get player and dealer hand values.

            while dealer_hand_value < 17: # while dealer hand is < 17 the dealer will add a card for each turn. 
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True) # at the end of the game show the dealers hand. 

            if self.check_winner(player_hand, dealer_hand):
                continue # if there is a winner, continue to next game

            print('Final Result')
            # player and dealer hand values.
            print('Your hand: ', player_hand_value)
            print('Dealer hand: ', dealer_hand_value)
            # show the value of the cards in the final result. 

            self.check_winner(player_hand, dealer_hand, True)
            # check_winner method to determine the winner of the current game. Pass True as third argument to indicate that it's the end of the game.

        print('Thanks for playing!')



    def check_winner(self, player_hand, dealer_hand, game_over=False): # win conditions
        # check game conditions when game is not over
        if not game_over:
            if player_hand.get_value() > 21:
                print('You busted. Dealer wins! 😭')
                return True
            elif dealer_hand.get_value() > 21:
                print('Dealer busted. You win! 🏆')
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print('Both players have blackjack! Tie! 😬')
                return True
            elif player_hand.is_blackjack():
                print('You have blackjack. You win! 🏆')
                return True
            elif dealer_hand.is_blackjack():
                print('Dealer has blackjack. You lose! 😭')
                return True # return true indicates that a win condition has been met and the game is over.
        else: # game is over
            if player_hand.get_value() > dealer_hand.get_value():
                print('You win! 🏆')
            elif player_hand.get_value() == dealer_hand.get_value():
                print('Tie! 😬')
            else:
                print('Dealer wins! 😭') 
    

g = Game()
g.play()
