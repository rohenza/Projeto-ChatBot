# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:45:55 2019

@author: augusto.coelho
"""

import Tokenize


def isPositive(text):
    if text in positiveAnswers:
        return True
    elif text in negativeAnswers:
        return False
    else:
        return None

def printSearch(text, corpus):
    searchResult = searchGame(text, corpus)
    print("Games: ")
    print("_________________________________")
    for game in sorted(searchResult.items(), reverse=True):
        #print(game[0], corpus[game[0]])
        gameC = corpus[game[0]]
        print("Name: ", gameC["name"])
        print("Price: ", gameC["price"])
        print("Description: ", gameC["deion"])
        print("_________________________________")


    return searchResult

def searchGame(text, corpus):

    text = Tokenize.tratarTexto(text)
    gameList = {}
    searchList = corpusTrat
    for key in searchList:
        searchList[key]["coe"] = Tokenize.coeficienteSimilaridade(text, searchList[key]["text"], searchList)
        if searchList[key]["coe"] > 0:
            gameList[key] = searchList[key]["coe"]
    return gameList

def getCorpus(corpus):
    searchList = corpus

    for key in corpus:
        searchList[key]["text"] = key + " " + corpus[key]["genre"] + " " + corpus[key]["deion"]

    return searchList

def isCreditCard(text):
    credit = Tokenize.nGram(text, "credit card")
    ticket = Tokenize.nGram(text, "bank ticket")
    if credit > ticket:
        return True
    elif ticket > credit:
        return False
    else:
        return None

positiveAnswers = ["yes", "yeah", "yeap", "y", "ye", "affirmative", "amen", "fine", "good", "ok", "okay", "true", "yea",
                   "all right", "aye", "beyond a doubt", "by all means", "certainly", "definitely", "even so",
                   "exactly", "gladly", "good enough", "granted", "indubitably", "just so", "most assuredly",
                   "naturally", "of course", "positively", "precisely", "sure thing", "surely", "undoubtedly",
                   "unquestionably", "very well", "willingly", "without fail", "yep"]

negativeAnswers = ["nay", "no", "negative", "not", "never", "nix", "n", "nop", "nope", "false"]




def corpusTratado(corpus):
    corpusTrat = getCorpus(corpus)
    for key in corpusTrat:
        corpusTrat[key]["text"] = Tokenize.tratarTexto(corpusTrat[key]["text"])
    return corpusTrat

corpus = {"league of legends": {"name": "league of legends", "price": 100.00, "genre": "moba",
                                "deion": "league of legends is a multiplayer online battle arena video game developed and published by Riot Games for microsoft windows and macos. the game follows a freemium model and is supported by microtransactions, and was inspired by the warcraft 3: the frozen throne mod, defense of the ancients."},
          "overwatch": {"name": "overwatch", "price": 150.00, "genre": "fps",
                        "deion": "slow down time, rain destruction from above in a jet-powered armor suit, or pilot a superpowered hamster ball: in overwatch, every hero has a unique set of devastating abilities."},
          "grand theft auto v": {"name": "grand theft auto v","price": 120.00, "genre": "action",
                                 "deion": "when a young street hustler, a retired bank robber and a terrifying psychopath find themselves entangled with some of the most frightening and deranged elements of the criminal underworld, the u.s. government and the entertainment industry, they must pull off a series of dangerous heists to survive in a ruthless city in which they can't trust each other."},
          "battlefield 4": {"name": "battlefield 4","price": 50.00, "genre": "fps",
                            "deion": "battlefield 4 is a first-person shooter video game developed by video game developer ea dice and published by electronic arts."},
          "street fighter v": {"name": "street fighter v","price": 80.00, "genre": "fight",
                               "deion": "experience the intensity of head-to-head battles with street fighter v! choose from 16 iconic characters, then battle against friends online or offline with a robust variety of match options."},
          "mortal kombat 11": {"name": "mortal kombat 11","price": 120.00, "genre": "fight",
                               "deion": "mortal kombat is back and better than ever in the next evolution of the iconic franchise."},
          "mortal kombat x": {"name": "mortal kombat x","price": 20.30, "genre": "fight",
                              "deion": "experience the next generation of the #1 fighting franchise. mortal kombat x combines unparalleled, cinematic presentation with all new gameplay."},
          "minecraft": {"name": "minecraft","price": 120.00, "genre": "adventure",
                        "deion": "it's a game about placing blocks and going on adventures. it’s set in infinitely-generated worlds of wide open terrain - icy mountains, swampy bayous, vast pastures and much more - filled with secrets, wonders and peril!"},
          "dragon ball fighter z": {"name": "dragon ball fighter ","price": 150.00, "genre": "fight",
                                    "deion": "dragon ball fighter z is born from what makes the dragon ball series so loved and famous: endless spectacular fights with its all-powerful fighters."},
          "naruto ultimate ninja storm": {"name": "naruto ultimate ninja storm","price": 80.00, "genre": "anime",
                                          "deion": "live the 4th great ninja war and its overpowering boss fights or defy your friends in ultra dynamic online and offline ninja confrontations!"},
          "death stranging": {"name": "death stranging","price": 220.00, "genre": "action-adventure",
                              "deion": "death stranding is an action game set in an open world, which also includes multiplayer functions. kojima compared the genre to how his earlier game metal gear – now considered to be a stealth game – was called an action game during its release because the stealth genre was not considered to exist at the time."},
          "nba2k 20": {"name": "nba2k 20","price": 120.00, "genre": "sports",
                       "deion": "2k continues to redefine what’s possible in sports gaming with nba 2k20, featuring best in class graphics & gameplay, ground breaking game modes, and unparalleled player control and customization."},
          "wwe 2k 19": {"name": "wwe 2k 19","price": 119.00, "genre": "sports",
                        "deion": "wwe 2k19 returns as the flagship wwe video game, with cover superstar aj styles! experience tons of creation options, match types and more!"},
          "just cause 3": {"name": "just cause 3","price": 43.00, "genre": "action-adventure",
                           "deion": "with over 1000 km² of complete freedom from sky to seabed, rico rodriguez returns to unleash chaos in the most creative and explosive ways imaginable."},
          "call of duty 3": {"name": "call of duty 3","price": 100.00, "genre": "fps", "deion": ""},
          "the elder scrolls": {"name": "the elder scrolls","price": 170.00, "genre": "rpg",
                                "deion": "winner of more than 200 game of the year awards, skyrim special edition brings the epic fantasy to life in stunning detail. the special edition includes the critically acclaimed game and add-ons with all-new features like remastered art and effects, volumetric god rays, dynamic depth of field, screen-space reflections, and more."},
          "lego batman": {"name": "lego batman","price": 12.50, "genre": "action-adventure",
                          "deion": "the caped crusader joins forces with the super heroes of the dc comics universe and blasts off to outer space to stop the evil brainiac from destroying earth."},
          }
corpusTrat = corpusTratado(corpus)
