import Tokenize

def isPositive(text):
    return True

def printSearch(text, corpus):
    searchResult = searchGame(text, corpus)
    for game in sorted(searchResult.items(), reverse=True):

        #print(game)
        print(game[0], corpus[game[0]])

def searchGame(text, corpus):

    text = Tokenize.tratarTexto(text)
    gameList = {}
    searchList = corpus

    for key in getCorpus(corpus):
        searchList[key]["coe"] = Tokenize.coeficienteSimilaridade(text, searchList[key]["text"], searchList)
        if searchList[key]["coe"] > 0:
            gameList[key] = searchList[key]["coe"]

    return gameList

def getCorpus(corpus):
    searchList = corpus

    for key in corpus:
        searchList[key]["text"] = key + " " + corpus[key]["genre"] + " " + corpus[key]["deion"]
    print(searchList)

    return searchList