import math

def tratarTexto(text):
    return text

def coeficienteSimilaridade(query, text, corpus):
    textBag = bag_of_words(text)
    soma = 0
    for word in textBag:
        dij = tf_idf(word, text, corpus)
        print(dij)
        wqj = tf_idf(word, query, corpus)
        soma += dij * 1
    print(soma)
    return soma

def bag_of_words(corpus):
    bag = []
    corpus = tratarTexto(corpus)
    for phrase in corpus:
        frase = standartize(phrase)
        for word in frase:
            if word not in bag:
                bag.append(word)

    return bag

def term_frequency(keyword, phrase):
    freq = 0
    phrase = standartize(phrase)
    for word in phrase:
        if word == keyword:
            freq = freq + 1

    return freq / (len(phrase))


def qntDocumentos_contendoTermo(keyword, corpus):
    docsContendoTermo = 0
    for frase in corpus:
        frase = standartize(frase)
        if (keyword in frase):
            docsContendoTermo = docsContendoTermo + 1

    return docsContendoTermo


def idf(keyword, corpus):
    N = (len(corpus))
    dft = qntDocumentos_contendoTermo(keyword, corpus)
    try:
        inv_document_frequency = math.log((N / dft), 10)
        return inv_document_frequency
    except:
        return None


def tf_idf(keyword, phrase, corpus):
    tf = term_frequency(keyword, phrase)
    invdf = idf(keyword, corpus)
    try:
        result = tf * invdf
        return result
    except:
        return 0


def standartize(phrase):

    phrase = phrase.replace(".", "")
    phrase = phrase.replace(",", "")
    phrase = phrase.replace("'", "")
    phrase = phrase.lower()
    phrase = phrase.split()

    return phrase

def tokenTreatment(text):
    return

def nGram(word1, word2):
    return

def regexEmail(text):
    return