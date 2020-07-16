#These imports are for the clear terminal feature (for tidying up the terminal)

import platform
import os

#This is a dictionary to define what the value of the card is.
define = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

#The introduction of the hand where each player and dealer is given two card each, shows total sum of each player (excluding dealer), shows bank amount and betted amount.
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

#This is to hide the last card of the dealer
    hand = copy.deepcopy(dealer.cards)
    hand[1] = '_'
    hand = str(hand).strip("[]").replace("'","")
    print(f"\nDealer's hand: {hand}")
    print("Total: ?")

#The choice begin shortly after the start defintion. This function will give the player an option to either 'hit' or 'stay' depending on what cards they get they may get a prompt of getting a 'bust' if card is over '21'.
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
            
            #This is the if statement that checks if the user goes above 21 and prompts the user that they've busted.
            if check(i) == True:
                print(f"{i.name.upper()} HAS BUSTED")
                break

#After all the players have made the choice the dealer will continue to make its own choice automatically, by following certain condition it will stay once its total is above 16 and hit if its total is below 17.
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

#Once the dealer makes its own choices the function will check if the players has won against the dealer or not. It also checks if it is tied with the dealer as well.
def winner():
    winner = []
    loser = []
    tie = []
    for i in players:
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
    
    for i in winner:
        i.add_bank()

    for i in loser:
        i.lose_bank()

    if len(winner) == 0 and len(tie) > 0:
        return "TIE"
    elif winner == []:
        return "DEALER"
    else:
        return winner

#After the 'winner' function checks who is the winner it will go through the finish function where it will evaluate who is the winner, show the winners hand, other players hand and dealers hand. (depending what was the outcome)
def finish(winner):
    print("\n\n__________________________________")
    if winner == "TIE":
        print("\nIT IS A TIE")
        for i in players:
            show_hand(i)
            print(f"Bank Total: {i.bank}")
        show_hand(dealer)
    elif winner == "BUST":
        print("\nALL HAS BUSTED")
        for i in players:
            show_hand(i)
            print(f"Bank Total: {i.bank}")
        show_hand(dealer)
    elif winner == "DEALER":
        print("DEALER WINS")
        for i in players:
            show_hand(i)
            print(f"Bank Total: {i.bank}")
        show_hand(dealer)
    else:
        for i in winner:
            print(f"\n{i.name.upper()} HAS WON!!")
            show_hand(i)
        show_hand(dealer)
        
#This function comes after the naming phase where the program will ask each player to place their appropriate bets.
def bet():
    for i in players:
        while True:
            try:
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
            except:
                print("\n__________________________________")
                print("\nPlease enter an integer number (E.G: 0 1 2 3 50 ...)")
                continue

#If one of the players or multiple has ran out of money this function will run through telling the player that they've ran out of money. The player will have the option to restart to their default value or to quit the game. Making the quitted player to be remove from the game permanently.
def check_amount():
    pop = []
    restart = False
    for i in players:
        if i.bank <= 0:
            print(f"\n{i.name.upper()} YOU HAVE NO MORE DOSH!!")
            print(f"\nBank Total: {i.bank}")
            while True:
                restart = input("\nWould you like to restart your bank with the value of 1000?     (yes/no)\n")
                if restart.lower() == "yes" or restart.lower() == "y":
                    i.bank = 1000
                    operating_system()
                    i.cards = []
                    dealer.cards = []
                    restart = True
                    break
                elif restart.lower() == "no" or restart.lower() == "n":
                    pop.append(players.index(i))
                    operating_system()
                    break
                else:
                    print("Please choose either 'Yes' or 'No'")
    #This function is to remove the player that has chosen to leave
    pop.reverse()
    for i in pop:
        players.pop(i)

    if len(players) == 0:
        return "EXIT"
    elif restart == True:
        return "RESTART"

#This function will ask the player how many players do they want to play in the game
def nth_player():
    while True:
        try:
            nth = input("\nHow many players?\n(Only up to 4 players)\n")
            if nth.lower() == 'exit':
                return exit_now.exit_game()
            nth = int(nth)
            if nth > 4 or nth < 1:
                print("\nPlease enter an integer number between 1 - 4")
            else: 
                break
        except:
            print("\nPlease enter an integer number (E.G: 1 2 3 4)")
    return nth

#This function deals with naming between each players/player
def names(nth):
    counter = 0
    if nth == None:
        return None
    while counter < nth:
        while True:
            name = input(f"\nPlease enter your name player {counter+1}...\n")
            name = name.split()
            if len(name[0]) < 2 or len(name[0]) > 20:
                print("\nPlease enter a name within the range of minimum 2 and maximum 20")
                continue
            elif len(name) == 1:
                players.append(name[0])
                counter += 1
                break
            elif len(name) > 1:
                print("\nPlease enter 1 word for your name")
                continue
            elif name[0].lower() == 'exit':
                exit = True
        
         
#The cardgen function will generate a deck of 52 cards and then it will shuffle it, creating randomness to the game
def cardgen():
    import random
    
    number = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    face = ['J', 'Q', 'K', 'A']
    
    deck = (number+face)*4
    random.shuffle(deck)
    return deck

#This is to check if the user has bust and check if the user has an 'A' in its hand and is above 21, this will convert the value 'A' from 11 to 1 from its unique defintion that each players get
def check(user):
    if 'A' in user.cards and total_sum(user) > 21:
        user.define_hand['A'] = 1
    if total_sum(user) > 21:
        user.bust = True
        return True

#This will calculate the total sum of the chosen players hand
def total_sum(user):
    total = 0
    for i in user.cards:
        total += user.define_hand[i]
    return total

#This will show the players the hand and the total sum of the hand of the chosen player
def show_hand(user):
    hand = str(user.cards).strip("[]").replace("'","")
    print(f"\n{user.name}'s hand: {hand}")
    print(f"Total: {total_sum(user)}")

#Start hand function is to give the chosen player 2 cards to start off the game
def start_hand(user):
    if deck == []:
        cardgen()
    for i in range(2):
        user.cards.append(deck[i])
    del deck[:2]
        
#Add card function will give the chosen player a card to its hand
def add_card(user):
    user.cards.append(deck[0])
    deck.pop(0)
    
#Function is to clear up the terminal. It will first check what operating system is being ran from and judging from that it will input the appropriate code to clear the terminal.
def operating_system():
    op = platform.system()
    if op == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

#Once the game has restarted all value of each players and dealer will revert back to its initial state
def reset():
    for i in players:
        i.bust = False
        i.define_hand['A'] = 11
    dealer.bust = False
    dealer.define_hand['A'] = 11

#At the end of the hand the players have the choice to exit the game or to continue the game.
def replay():
    while True:
        replay = input("\n\nWould you like to continue with the game?     (Yes/No)\n")
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

#An object orienting class 'Player' once created will give each player their own unique values.
class Player():
    import copy
    define_hand = copy.deepcopy(define)
    def __init__(self, name, bank, bet, bust, cards):
        self.cards = cards
        self.name = name
        self.bank = bank
        self.bet = bet
        self.bust = bust

    #Minuses the bet from the bank
    def lose_bank(self):
        self.bank -= self.bet

    #Adds the bet to the bank
    def add_bank(self):
        self.bank += self.bet

class Exit_Check():
    def __init__(self, exit):
        self.exit = exit

    def exit_game(self):
        self.exit = True

#An object orienting class 'Dealer' once created will give the dealer its own unique values.
class Dealer():
    import copy
    define_hand = copy.deepcopy(define)
    def __init__(self, name, bust, cards):
        self.cards = cards
        self.name = name
        self.bust = bust

# Game Start

print("Welcome to Blackjack")
print("\nThe goal of the game is to get as close to 21 as possible and have the total higher than the dealer!\n")
print("\n you can quit the game by writing down 'exit' ")
players = []
deck = cardgen()
exit_now = Exit_Check(False)
names(nth_player())
for i in range(len(players)):
    players[i] = Player(players[i], 1000, 0, False, [])
dealer = Dealer("Dealer", False, [])


while True:
    if exit_now.exit == True: break
    reset()
    bet()
    if exit_now.exit == True: break
    start()
    choice()
    if exit_now.exit == True: break
    ai()
    finish(winner())
    again = check_amount()
    if again == "RESTART":
        continue
    if again == "EXIT":
        break
    if replay():
        break
