import Tokenize
import Answers
import time


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


class CreditCard(object):
    def __init__(self):
        pass


searchList = {}
order = Order()
order.creditCard = CreditCard()

class SearchState(object):

    def answer(self, text):
        Answers.printSearch(text, corpus)
        print("Is it one of those games you were looking for or do you want to search again? ")
        return SearchAgainState()


class SearchAgainState(object):

    def answer(self, text):
        if Answers.isPositive(text):
            print("What game would you like to search?")
            return SearchState()
        elif not Answers.isPositive(text):
            print("What's the name of the game?")
            return GameNameState()
        else:
            print("Sorry, I didn't understand what you meant, can you be more specific?")
            return SearchAgainState()


class GameNameState(object):

    def answer(self, text):
        list = order.searchList
        for game in list:
            list[game]["ngram"] = Tokenize.nGram(game, text)
        list = sorted(list.items(), reverse=True)
        order.game = list[0]
        print("Is this the game you are looking for?")
        print(order.game)
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
        order.email = text
        print("What's your CPF?")
        return CPFState()


class CPFState(object):

    def answer(self, text):
        order.cpf = text
        print("How do you want to pay? Credit card or bank ticket?")
        return PaymentMethodState()


class PaymentMethodState(object):

    def answer(self, text):
        if Answers.isCreditCard(text):
            print("You choose Credit Card. How many installments?")
            return PaymentInstallmentsState()
        else:
            print("You choose Bank Ticket. You will be able to download your game after the payment confirmation.")
            print("Download your ticket, pay it and them you will receive and email with the download link.")
            print("Bank Ticket")
            print("Do you want to buy another game?")
            return StartAgainState()


class PaymentInstallmentsState(object):

    def answer(self, text):
        order.creditCard.installments = text
        print("What is the number of the Credit Card?")
        return CreditCardNumberState()


class CreditCardNumberState(object):

    def answer(self, text):
        order.creditCard.expirationDate = text
        print("What is the expiration date of the Credit Card?")
        return CardExpirationTimeState()


class CardExpirationTimeState(object):

    def answer(self, text):
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
        print("We are verifying your Credit Card information. Wait a moment.")
        time.sleep(5)
        print("We are all set. Your Credit Card is valid.")
        print("Let's see your order: ")
        for game in order.games:
            print(game.key() + " price: " + str(game["price"]))
        print("Total: " + str(order.total))
        return ConfirmCreditCardState()


class ConfirmCreditCardState(object):
    def answer(self, text):
        if Answers.isPositive(text):
            print("Your order is complete. You can download your games now.")
            print("Do you want to start another order?")
            return StartAgainState()
        elif not Answers.isPositive(text):
            print("Do you want to start another order?")
            return StartAgainState()
        else:
            print("Sorry, I didn't understand what you meant, can you be more specific?")
            return ConfirmCreditCardState()

class StartAgainState(object):
    def answer(self, text):
        if Answers.isPositive(text):
            return SearchState()
        elif not Answers.isPositive(text):
            return None
        else:
            print("Sorry, I didn't understand what you meant, can you be more specific?")
            return StartAgainState()

corpus = {"league of legends": {"price": 100.00, "genre": "moba",
                                "deion": "league of legends is a multiplayer online battle arena video game developed and published by Riot Games for microsoft windows and macos. the game follows a freemium model and is supported by microtransactions, and was inspired by the warcraft 3: the frozen throne mod, defense of the ancients."},
          "overwatch": {"price": 150.00, "genre": "fps",
                        "deion": "slow down time, rain destruction from above in a jet-powered armor suit, or pilot a superpowered hamster ball: in overwatch, every hero has a unique set of devastating abilities."},
          "grand theft auto v": {"price": 120.00, "genre": "action",
                                 "deion": "when a young street hustler, a retired bank robber and a terrifying psychopath find themselves entangled with some of the most frightening and deranged elements of the criminal underworld, the u.s. government and the entertainment industry, they must pull off a series of dangerous heists to survive in a ruthless city in which they can't trust each other."},
          "battlefield 4": {"price": 50.00, "genre": "fps",
                            "deion": "battlefield 4 is a first-person shooter video game developed by video game developer ea dice and published by electronic arts."},
          "street fighter v": {"price": 80.00, "genre": "fight",
                               "deion": "experience the intensity of head-to-head battles with street fighter v! choose from 16 iconic characters, then battle against friends online or offline with a robust variety of match options."},
          "mortal kombat 11": {"price": 120.00, "genre": "fight",
                               "deion": "mortal kombat is back and better than ever in the next evolution of the iconic franchise."},
          "mortal kombat x": {"price": 20.30, "genre": "fight",
                              "deion": "experience the next generation of the #1 fighting franchise. mortal kombat x combines unparalleled, cinematic presentation with all new gameplay."},
          "minecraft": {"price": 120.00, "genre": "adventure",
                        "deion": "it's a game about placing blocks and going on adventures. it’s set in infinitely-generated worlds of wide open terrain - icy mountains, swampy bayous, vast pastures and much more - filled with secrets, wonders and peril!"},
          "dragon ball fighter z": {"price": 150.00, "genre": "fight",
                                    "deion": "dragon ball fighter z is born from what makes the dragon ball series so loved and famous: endless spectacular fights with its all-powerful fighters."},
          "naruto ultimate ninja storm": {"price": 80.00, "genre": "anime",
                                          "deion": "live the 4th great ninja war and its overpowering boss fights or defy your friends in ultra dynamic online and offline ninja confrontations!"},
          "death stranging": {"price": 220.00, "genre": "action-adventure",
                              "deion": "death stranding is an action game set in an open world, which also includes multiplayer functions. kojima compared the genre to how his earlier game metal gear – now considered to be a stealth game – was called an action game during its release because the stealth genre was not considered to exist at the time."},
          "nba2k 20": {"price": 120.00, "genre": "sports",
                       "deion": "2k continues to redefine what’s possible in sports gaming with nba 2k20, featuring best in class graphics & gameplay, ground breaking game modes, and unparalleled player control and customization."},
          "wwe 2k 19": {"price": 119.00, "genre": "sports",
                        "deion": "wwe 2k19 returns as the flagship wwe video game, with cover superstar aj styles! experience tons of creation options, match types and more!"},
          "just cause 3": {"price": 43.00, "genre": "action-adventure",
                           "deion": "with over 1000 km² of complete freedom from sky to seabed, rico rodriguez returns to unleash chaos in the most creative and explosive ways imaginable."},
          "call of duty 3": {"price": 100.00, "genre": "fps", "deion": ""},
          "the elder scrolls": {"price": 170.00, "genre": "rpg",
                                "deion": "winner of more than 200 game of the year awards, skyrim special edition brings the epic fantasy to life in stunning detail. the special edition includes the critically acclaimed game and add-ons with all-new features like remastered art and effects, volumetric god rays, dynamic depth of field, screen-space reflections, and more."},
          "lego batman": {"price": 12.50, "genre": "action-adventure",
                          "deion": "the caped crusader joins forces with the super heroes of the dc comics universe and blasts off to outer space to stop the evil brainiac from destroying earth."},
          }

Answers.printSearch("fight", corpus)
