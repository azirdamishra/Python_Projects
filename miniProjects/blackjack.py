#rules to play the game
'''
To play a hand of Blackjack the following steps must be followed:

Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again

'''

import random

#declare global variables 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

playing = True


#create Card class for creating a separate object for each card in deck
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'


#create a deck class which stores 52 objects in a list that can later be shuffled
class Deck:
    
    #we instantiate all 52 card objects and add them to our list in the __init__ method
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank)) #build card objects with the suit and rank
    
    #to print out the whole card deck all at once if needed 
    def __str__(self):     
        deck_composition = '' 
        for card in self.deck:
            deck_composition += '\n' + card.__str__() #add each card object's print string
        return 'The deck has ' + deck_composition

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


#this class holds objects dealt from the deck and is used to keep track of the 
#value in the player's hand
class Hand:
    def __init__(self):
        self.cards = []  #an empty list 
        self.value = 0   #ero value of the hand in the beginning
        self.aces = 0    # an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]     #don't need to always add the argument to the __init method, you can add to other functions and give specific arguments when calling them 
        if card.rank == 'Ace':
            self.aces +=1
            
    def adjust_for_ace(self):
        if self.value >= 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            

#to keep track, deduct and add to the player's chips
#could also be done using global variables as mentioned before the final gameplay**
class Chips:
    
    def __init__(self, total = 100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


#Defining independent functions

#func for taking bets
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please enter a bet according to the available chips: '))
        except:
            print('Please try again')
            continue
        else:
            if chips.bet > chips.total:
                print('Bet cannot exceed ' + chips.total )
            else:
                break
                
#its always better for the functions to be self contained and accept arguments rather than carrying forth values 
#from other functions as the program won't completely stop


#either player takes hits until they bust 
#hit function can also be defined inside the hit_or_stand()
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to hit or stand? Please enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck, hand) #acc to hit() defined above
        elif x[0].lower() == 's':
            print('Player stands. Dealer plays.')
            playing = False
        else:
            print('Sorry.Please try again}')
            continue
        break


#func to display cards to the player, only one of the two of the dealer in the middle of the game
def show_some(player,dealer):
    print('\nDealers Hand:') #dealer and player are objects of class Hand()
    print('<Cards hidden>')
    print(dealer.cards[0])
    print('Players Hand:', *player.cards, sep='\n')

#shows all cards of player and dealer at the end of playing    
def show_all(player,dealer):
    print('\nDealers Hand:' , *dealer.cards, sep='\n')
    print('Dealers value', dealer.value)
    print('Players Hand', *player.cards, sep='\n')
    print('Players value', player.value)


#handling different game scenarios
def player_busts(player,dealer, chips):
    print('Player busts')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player wins')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Dealer busts')
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print('Dealer wins')
    chips.lose_bet()
    
def push(player, dealer):
    print('Dealer and Player tie. Its a push.')


#**in this game even if we continue playing the old total amount is not carried forward and we always start with 
#a total of 100

#later i will create a separate game where I try to add a global variable called total_money and that can keep getting added acc to the input 
#of the player and the final amount can get carried forward 
#this variable can get added inside the overall while loop only

while True:
    # Print an opening statement
    print('Hello and welcome to Blackjack: the economical version!')
    print('Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
    # Set up the Player's chips
    
    chips = Chips() #letting the base value of chips be 100 for now we can promt user later
    
    
    # Prompt the Player for their bet
    take_bet(chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player) #this contains the variable playing which would turn false and exit loop
        
        
        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player, dealer, chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        
        while dealer.value <17:
            hit(deck, dealer)
    
        # Show all cards
        show_all(player, dealer)
    
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player, dealer, chips)
        
        elif dealer.value > player.value:
            dealer_wins(player, dealer, chips)
        
        elif dealer.value < player.value:
            player_wins(player, dealer, chips)
            
        else:
            push(player, dealer)
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",chips.total)
    
    # Ask to play again
    new_game = input('Do you want to play again? enter yes or no')
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else: 
        print('Thanks for playing!')

        break



