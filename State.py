# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:45:56 2019

@author: augusto.coelho
"""

import Tokenize
import Answers
import time


class CreditCard(object):
    def __init__(self):
        pass


class SearchState(object):

    def answer(self, text):
        order.searchList = Answers.printSearch(text, Answers.corpus)
        print("Do you want to search again? ")
        return SearchAgainState()


class SearchAgainState(object):

    def answer(self, text):
        choose = Answers.isPositive(text)
        if choose:
            print("What game would you like to search?")
            return SearchState()
        elif choose == False:
            print("What's the name of the game?")
            return GameNameState()
        else:
            print("Sorry, I didn't understand what you meant, can you be more specific?")
            return SearchAgainState()


class GameNameState(object):

    def answer(self, text):
        list = order.searchList

        for game in list:
            list[game] = Tokenize.nGram(game, text)

        list = sorted(list.items(), key =
             lambda kv:(kv[1], kv[0]), reverse=True)
        order.game = Answers.corpus[list[0][0]]
        print("Is this the game you are looking for?")
        gameC = order.game
        print("_________________________________")
        print("Name: ", gameC["name"])
        print("Price: ", gameC["price"])
        print("Description: ", gameC["deion"])
        print("_________________________________")
        return ConfirmGameState()


class ConfirmGameState(object):

    def answer(self, text):
        if Answers.isPositive(text):
            order.games.append(order.game)
            order.total += order.game["price"]
            print("Do you want to add another game?")
            return AddAnotherGameState()
        elif not Answers.isPositive(text):
            print("What's the name of the game?")
            return GameNameState()
        else:
            print("Sorry, I didn't understand what you meant, can you be more specific?")
            return ConfirmGameState()


class AddAnotherGameState(object):

    def answer(self, text):
        if Answers.isPositive(text):
            print(" What game do you want??")
            return SearchState()
        elif not Answers.isPositive(text):
            print("What's your name?")
            return UserNameState()
        else:
            print("Sorry, I didn't understand what you meant, can you be more specific?")
            return ConfirmGameState()


class UserNameState(object):

    def answer(self, text):
        order.name = text
        print("What's your email?")
        return UserEmailState()


class UserEmailState(object):

    def answer(self, text):
        if not Tokenize.valid_email(text):
            print("Invalid email. Please enter a valid email.")
            return UserEmailState()
        order.email = text
        print("What's your CPF? Enter only numbers.")
        return CPFState()


class CPFState(object):

    def answer(self, text):
        if not Tokenize.valid_cpf(text):
            print("Invalid CPF. Please enter again with only number.")
            return CPFState()
        order.cpf = text
        print("How do you want to pay? Credit card or bank ticket?")
        return PaymentMethodState()


class PaymentMethodState(object):

    def answer(self, text):
        choose = Answers.isCreditCard(text)
        if choose:
            print("You choose Credit Card. How many installments?")
            return PaymentInstallmentsState()
        elif not choose:
            print("You choose Bank Ticket. You will be able to download your game after the payment confirmation.")
            print("Download your ticket, pay it and them you will receive and email with the download link.")
            print("Bank Ticket")
            print("Do you want to buy another game?")
            return StartAgainState()
        else:
            print("Sorry, I didn't understand what you meant, can you be more specific?")
            print("How do you want to pay? Credit card or bank ticket?")
            return PaymentMethodState


class PaymentInstallmentsState(object):

    def answer(self, text):
        order.creditCard.installments = text
        print("What is the number of the Credit Card?")
        return CreditCardNumberState()


class CreditCardNumberState(object):

    def answer(self, text):
        if not Tokenize.valid_card_number(text):
            print("Enter a valid credit card number.")
            return CreditCardNumberState()
        order.creditCard.expirationDate = text
        print("What is the expiration date of the Credit Card? Format mm/yy")
        return CardExpirationTimeState()


class CardExpirationTimeState(object):

    def answer(self, text):
        if not Tokenize.valid_exp_date(text):
            print("Enter a valid expiration date. Format mm/yy")
            return CardExpirationTimeState()
        order.creditCard.holder = text
        print("What is the name of the holder of the Credit Card?")
        return CardholderState()


class CardholderState(object):

    def answer(self, text):
        order.creditCard.verification = text
        print("What is the verification code of the Credit Card?")
        return VerificationCodeState()


class VerificationCodeState(object):

    def answer(self, text):
        if not Tokenize.valid_conf_code(text):
            print("Enter a valid verification code")
            return VerificationCodeState()
        print("We are verifying your Credit Card information. Wait a moment.")
        time.sleep(3)
        print("We are all set. Your Credit Card is valid.")
        print("Let's see your order: ")
        for game in order.games:
            print(game['name'] + " price: " + str(game['price']))
        print("Total: " + str(order.total))
        print("Do you want to proceed with the order?")
        return ConfirmCreditCardState()


class ConfirmCreditCardState(object):
    def answer(self, text):
        if Answers.isPositive(text):
            print("Your order is complete. You can download your games now.")
            print("Do you want to start another order?")
            return StartAgainState()
        elif Answers.isPositive(text) == False:
            print("Do you want to start another order?")
            return StartAgainState()
        else:
            print("Sorry, I didn't understand what you meant, can you be more specific?")
            return ConfirmCreditCardState()

class StartAgainState(object):
    def answer(self, text):
        if Answers.isPositive(text):
            print("What game would you like to search?")
            return SearchState()
        elif not Answers.isPositive(text):
            return None
        else:
            print("Sorry, I didn't understand what you meant, can you be more specific?")
            return StartAgainState()


class Order(object):
    def __init__(self):
        self.searchList = {}
        self.name = ""
        self.total = 0
        self.games = []
        self.game = {}
        self.email = ""
        self.cpf = ""
        self.state = SearchState()

    def answer(self, text):
        self.state = self.state.answer(text)





searchList = {}
order = Order()
order.creditCard = CreditCard()





