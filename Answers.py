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
    searchList = getCorpus(corpus)
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