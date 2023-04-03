import re


def cleanData(words: list) -> list:

    for i in range(len(words)):
        words[i] = re.sub(r'[,\'./()]|\sBD',r'', words[i])
    return words
