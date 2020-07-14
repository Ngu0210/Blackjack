import platform
import os

define = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

def start():
    import copy

    print("\n\n__________________________________")
    print("\nGame has begun...")   

    for i in players:
        start_hand(i)
    start_hand(dealer)
    for i in players:
        check(i)
    check(dealer)
    for i in players:
        show_hand(i)
        print(f"Total Bank: {i.bank}")
        print(f"Betted Amount: {i.bet}")

    hand = copy.deepcopy(dealer.cards)
    hand[1] = '_'
    hand = str(hand).strip("[]").replace("'","")
    print(f"\nDealer's hand: {hand}")
    print("Total: ?")

def choice():
    for i in players:
        print("\n\n__________________________________")
        print(f"{i.name.upper()}'S TURN")
        show_hand(i)

        while True:

            print("\n\n__________________________________")

            decision = str(input("\nHIT or STAY\n"))

            if decision.lower() == 'hit':
                add_card(i)
                check(i)
                show_hand(i)
                
                print(f"\nBank Total: {i.bank}")
                print(f"Betted Amount: {i.bet}")

            elif decision.lower() == 'stay':
                break

            else:
                print("Please input either 'HIT' or 'STAY'")
            
            if check(i) == True:
                print(f"{i.name.upper()} HAS BUSTED")
                break

def ai():
    while True:
        if total_sum(dealer) < 17:
            add_card(dealer)
        elif total_sum(dealer) > 16:
            break
        if check(dealer) == True:
            show_hand(dealer)
            print("DEALER HAS BUSTED")
            break                       

def winner():
    winner = []
    loser = []
    tie = []
    for i in players:
        if len(players) == 1:
            winner.append(i)
        else:
            if i.bust != True:
                if dealer.bust == True:
                    winner.append(i)
                elif dealer.bust != True:
                    if total_sum(i) > total_sum(dealer):
                        winner.append(i)
                    elif total_sum(i) == total_sum(dealer):
                        tie.append(i)
                    else:
                        loser.append(i)
            else:
                loser.append(i)
    
    if len(winner) == 0 and len(tie) > 0:
        return "TIE"
                    
    for i in winner:
        i.add_bank()

    for i in loser:
        i.lose_bank()

    if winner == []:
        return "DEALER"
    else:
        return winner


def finish(winner):
    print("\n\n__________________________________")
    if winner == "TIE":
        print("\nIT IS A TIE")
        for i in players:
            show_hand(i)
            print(f"Total: {total_sum(i)}")
        show_hand(dealer)
    elif winner == "BUST":
        print("\nALL HAS BUSTED")
        for i in players:
            show_hand(i)
            print(f"Total: {total_sum(i)}")
        show_hand(dealer)
    elif winner == "DEALER":
        for i in players:
            show_hand(i)
            print(f"Total: {total_sum(i)}")
        show_hand(dealer)
    else:
        for i in winner:
            print(f"\n{i.name.upper()} HAS WON!!")
            show_hand(i)
        show_hand(dealer)
        

def bet():
    while True:
        try:
            for i in players:
                while True:
                    print("\n__________________________________")
                    print(f"\nBank Total: {i.bank}")
                    amount = int(input(f"\nEnter your bet {i.name}\n"))
                    if amount > i.bank:
                        print("This is over your bank budget!")   
                        print("please choose an appropriate amount corresponding to you bank amount")
                    elif amount < 0:
                        print("please choose an appropriate amount corresponding to you bank amount")
                    elif amount == 0:
                        print("Amount must be above zero")
                    else:
                        i.bet = amount
                        break
            break
        except:
            print("\n__________________________________")
            print("\nPlease enter an interger number (E.G: 0 1 2 3 50 ...)")
            continue

def check_amount():
    pop = []
    for i in players:
        if i.bank <= 0:
            print(f"\n{i.name.upper()} YOU HAVE NO MORE DOSH!!")
            print(f"\nBank Total: {i.bank}")
            while True:
                restart = input("\nWorld you like to restart?     (yes/no)\n")
                if restart.lower() == 'yes':
                    i.bank = 1000
                    operating_system()
                    i.cards = []
                    dealer.cards = []
                    return "RESTART"
                elif restart.lower() == 'no':
                    pop.append(players.index(i))
                    operating_system()
                    break
                else:
                    print("Please choose either 'Yes' or 'No'")

    pop.reverse()
    for i in pop:
        players.pop(i)

    if len(players) == 0:
        return "EXIT"

def nth_player():
    while True:
        try:
            nth = int(input("\nHow many players?\n(Only up to 4 players)\n"))
            if nth > 4 or nth < 1:
                print("\nPlease enter an interger number between 1 - 4")
            else: 
                break
        except:
            print("\nPlease enter an interger number (E.G: 1 2 3 4)")
    return nth

def names(nth):
    counter = 0
    while counter < nth:
        name = input("\nPlease enter your name...\n")
        players.append(name)
        counter += 1
         
def cardgen():
    import random
    
    number = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    face = ['J', 'Q', 'K', 'A']
    
    deck = (number+face)*4
    random.shuffle(deck)
    return deck

def check(user):
    if 'A' in user.cards and total_sum(user) > 21:
        user.define_hand['A'] = 1
    if total_sum(user) > 21:
        user.bust = True
        return True

def total_sum(user):
    total = 0
    for i in user.cards:
        total += user.define_hand[i]
    return total

def show_hand(user):
    hand = str(user.cards).strip("[]").replace("'","")
    print(f"\n{user.name}'s hand: {hand}")
    print(f"Total: {total_sum(user)}")

def start_hand(user):
    for i in range(2):
        user.cards.append(deck[i])
    del deck[:2]
        
def add_card(user):
    user.cards.append(deck[0])
    deck.pop(0)
    

def operating_system():
    op = platform.system()
    if op == 'Darwin':
        os.system('clear')
    elif op == 'Windows':
        os.system('cls')
    elif op == 'Linux':
        os.system('clear')
    else:
        os.system('clear')

def reset():
    for i in players:
        i.bust = False
        i.define_hand['A'] = 11
    dealer.bust = False
    dealer.define_hand['A'] = 11
class Player():
    import copy
    define_hand = copy.deepcopy(define)
    def __init__(self, name, bank, bet, bust, cards):
        self.cards = cards
        self.name = name
        self.bank = bank
        self.bet = bet
        self.bust = bust

    def lose_bank(self):
        self.bank -= self.bet

    def add_bank(self):
        self.bank += self.bet

class Dealer():
    import copy
    define_hand = copy.deepcopy(define)
    def __init__(self, name, bust, cards):
        self.cards = cards
        self.name = name
        self.bust = bust

def replay():
    while True:
        replay = input("\n\nContinue?     (Yes/No)\n")
        if replay.lower() == 'yes' or replay.lower() == 'y':
            operating_system()
            for i in players:
                i.cards = []
            dealer.cards = []
            break
        elif replay.lower() == 'no' or replay.lower() == 'n':
            operating_system()
            return True
        else:
            print("Please choose either 'Yes' or 'No'")

# Game Start

print("Welcome to Blackjack")
print("\nThe goal of the game is to get as close to 21 as possible and have the total higher then the dealer!\n")

players = []
deck = cardgen()
names(nth_player())
for i in range(len(players)):
    players[i] = Player(players[i], 1000, 0, False, [])
dealer = Dealer("Dealer", False, [])

while True:
    reset()
    bet()
    start()
    choice()
    ai()
    finish(winner())
    again = check_amount()
    if again == "RESTART":
        continue
    if again == "EXIT":
        break
    if replay():
        break
