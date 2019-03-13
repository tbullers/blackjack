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
        f"You start with a bankroll of ${start_bank_role}.  Your least bet is ${min_bet}.\n\n"
    )
    print("Good luck!\n\n")


# amounts should be positive integers.  This class check to see if input string can be cast to an int
# and if it is a positive integer.  It returns a tuple with True or False indicating if the string is a valid integer
# and the sanitized integer value.  Returns (False, None) if not valid
def sanitize_input(amount_string):
    result = False
    value = None
    try:
        value = int(amount_string)
        if value >= 0:
            result = True
    except:
        pass
    return result


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
            return (
                True,
                "The account was created and the current balance is: $ " + self.balance,
            )
        else:
            return (False, "There was an error - the account was not created")

    def deposit(amount):
        (valid, amount) = sanitize_input(amount)
        if valid:
            self.balance += amount
            return (True, "The amount was deposited")
        else:
            return (False, "There was an error and the deposit did not proceed.")

    def withdraw(amount):
        (valid, amount) = sanitize_input(amount)
        if valid:
            self.balance -= amount
            return (
                True,
                "The amount was withdrawn and the new balance is: $" + self.balance,
            )
        else:
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
        return ranks[self.rank]

    def color(self):
        return suits[self.suit]


class Deck:
    def __init__(self):
        print("creating cardlist")
        global ranks, suits
        self.cardlist = []
        for suit in suits:
            print("The suite is: " + suit)
            for rank in ranks:
                print("The rank is: " + rank)
                self.cardlist.append(Card(rank, suit))
        random.shuffle(self.cardlist)

    def __str__(self):
        string = ""
        for card in self.cardlist:
            string += str(card.rank + "-" + card.suit + "\n")
        return string


class hand:
    pass


if __name__ == "__main__":
    ranks = {
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
    suits = {"Hearts": "Red", "Diamonds": "Red", "Spades": "Black", "Clubs": "Black"}
    start_bank_role = 100
    min_bet = 1

    intro_text()
    player_account = CreateAccount(start_bank_role)
    while ready_to_play():
        deck = Deck()
        print("The dealer has a new shuffled deck.")
        print(deck)
        print("Your account balance is $ " + player_account.balance() + "\n")
    while True:
        dealer_hand = deck.draw(2)
        print("Your account balance is $ " + player_account.balance() + "\n")
        response = str(
            input(
                "How much would you like to bet? (must be between $ "
                + min_bet
                + " and $ "
                + player_account.balance()
            )
        )
        (isvalid, amount) = sanitize_input(response)
        if isvalid and (amount >= min_bet):
            break
    player_account.withdraw(amount)
    print("Your new balance is: $ " + player_account.balance())
