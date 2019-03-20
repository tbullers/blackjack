#!/usr/bin/python

import random

"""
Here's a blackjack game as a project for the udemy python online training class
"""


def intro_text():
    print("\n*** Black Jack ***\n\n")
    print("You'll be playing against the dealer (computer)")
    print("Ask for a Hit to get a new card or Stand to let the dealer play.")
    print("Player whose hand is closest to 21, wins the game.")
    print(
        f"You start with a bankroll of ${START_BANK_ROLE}.  Your least bet is ${MIN_BET}.\n\n"
    )
    print("Good luck!\n\n")


# See if passed value is a positive integer.  Return a tuple with values (valid flag, integer amount)
# If not an integer, returns a tuple (False, None)
# If is an integer, and value is less than zero, returns (False, value)
# If is a positive integer, then returns (True, value)


def sanitize_input(amount_string):
    try:
        value = int(amount_string)
    except:
        return (False, None)

    if value < 1:
        return (False, value)
    return (True, value)


def ready_to_play():
    while True:
        response = str(input("Are you ready to play? (y/n)")).lower()
        if response == "y":
            return True
        elif response == "n":
            return False


class CreateAccount:
    def __init__(self, start_balance):
        (valid, amount) = sanitize_input(start_balance)
        if valid:
            self.balance = amount
        else:
            raise ValueError(
                "Error - the value in an invalid starting balance - must be a positive integer"
            )

    def deposit(self, amount):
        (valid, amount) = sanitize_input(amount)
        if valid:
            self.balance += amount
            return (True, "The amount was deposited")
        else:
            return (False, "There was an error and the deposit did not proceed.")

    def withdraw(self, amount):
        (valid, amount) = sanitize_input(amount)
        if valid:
            self.balance -= amount
            return (
                True,
                "The amount was withdrawn and the new balance is: $" + self.balance,
            )
        return (
            False,
            "There was an error and the withdrawal did not proceed.  The balance is: $"
            + self.balance,
            )


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.rank) + " " + str(self.suit)

    def value(self):
        return RANKS[self.rank]

    def color(self):
        return SUITS[self.suit]


class Deck:
    def __init__(self):
#        print("creating cardlist")
        global RANKS, SUITS
        self.cardlist = []
        for suit in SUITS:
#            print("The suite is: " + suit)
            for rank in RANKS:
#               print("The rank is: " + rank)
                self.cardlist.append(Card(rank, suit))
        random.shuffle(self.cardlist)

    def __str__(self):
        string = ""
        for card in self.cardlist:
            string += str(card.rank + "-" + card.suit + "\n")
        return string


class Hand:
    pass


if __name__ == "__main__":
    RANKS = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11,
    }
    SUITS = {"Hearts": "Red", "Diamonds": "Red", "Spades": "Black", "Clubs": "Black"}
    START_BANK_ROLE = 100
    MIN_BET = 1

    intro_text()

    try:
        player_account = CreateAccount(START_BANK_ROLE)
    except:
        print("Cannot create an account - bad initial bank role amount")

    print("the player's balance is ->" + str(player_account.balance))

    while ready_to_play():
        deck = Deck()
        print("The dealer has a new shuffled deck.")
#        print(deck)
        print("Your account balance is $ " + str(player_account.balance) + "\n")

        while True:
#           dealer_hand = deck.draw(2)
            print("Your account balance is $ " + str(player_account.balance) + "\n")
#            response = (input("How much would you like to bet? (must be between $ "+MIN_BET+" and $ "+str(player_account.balance))
            response = (input("How much would you like to bet ?:"))
            (isvalid, amount) = sanitize_input(response)
            if isvalid and (amount >= MIN_BET):
                break
    player_account.withdraw(amount)
    print("Your new balance is: $ " + player_account.balance())
