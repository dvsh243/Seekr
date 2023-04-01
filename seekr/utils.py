import re


def cleanData(words: list) -> list:

    for i in range(len(words)):
        words[i] = re.sub(r'[,\'./#!()]|\sBD',r'', words[i])
    return words


def generateNGrams(words: list, n: int = 3) -> list:
    ngramWords = []

    for word in words:
        ngrams = []

        # print(word)
        for i in range(n - 1, len(word) + 1):
            # print("'" + word[i - n: i] + "'", end=' -- ')
            ngrams.append( word[i - n + 1: i + 1] )
        # print('\n')
    
        ngramWords.append(ngrams)

    return ngramWords