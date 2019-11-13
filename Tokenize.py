import math
import re


def tratarTexto(text):
    return text


def coeficienteSimilaridade(query, text, corpus):
    textBag = bag_of_words(corpus)
    soma = 0
    for word in textBag:
        dij = tf_idf(word, text, corpus)
        wqj = tf_idf(word, query, corpus)
        soma += dij * wqj
    return soma


def bag_of_words(corpus):
    bag = []
    text = []
    for key in corpus:
        text.append(tratarTexto(corpus[key]["text"]))
    for phrase in text:
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
        frase = standartize(corpus[frase]["text"])
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


def nGram(word1, word2):
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")

    diagramWord1 = diagram(word1)
    diagramWord2 = diagram(word2)

    contador = 0

    for i in diagramWord1:
        if i in diagramWord2:
            contador += 1
    nGram = 2 * contador / (len(diagramWord1) + len(diagramWord2))
    return nGram


def diagram(word):
    list = []
    for cont in range(len(word) - 1):
        diagram = word[cont] + word[cont + 1]
        if diagram not in list:
            list.append(diagram)

    return list


def valid_email(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def valid_cpf(text):
    return bool(re.search(r"[0-9]{11}$", text))


def valid_exp_date(text):
    return bool(re.search(r"[0-1]{1}[0-9]{1}/[2-3]{1}[0-9]{1}$", text))


def valid_conf_code(text):
    return bool(re.search(r"[0-9]{3}$", text))

def valid_card_number(text):
    return bool(re.search(r"[0-9]{16}$", text))

