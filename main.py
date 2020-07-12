def cardgen():
    import random
    
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    face = ['J', 'Q', 'K', 'A']
    
    deck = (number+face)*4
    random.shuffle(deck)
    return deck



def start_hand(user):
    for i in range(2):
        user.cards.append(deck[i])
    del deck[:2]
        

class Player():
    def __init__(self, name, cards=[]):
        self.cards = cards
        self.name = name

class Dealer():
    def __init__(self, cards=[]):
        self.cards = cards

define = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
deck = cardgen()

# Game Start

print("Welcome to Blackjack")
print("\nThe goal of the game is to get as close to 21 as possible and have the total higher then the dealer!\n")
name = input("\nPlease enter your name...\n")
player = Player(name)
dealer = Dealer()
start_hand(player)
start_hand(dealer)
print(f"{name}:{player.cards}")
print(f"Dealer:{dealer.cards}")

