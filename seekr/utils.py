import re


def cleanData(words: list) -> list:

    for i in range(len(words)):
        words[i] = re.sub(r'[,\'./()]|\sBD',r'', words[i])
    return words


def ngrams(string, n=3):
    string = re.sub(r'[,-./]|\sBD',r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]


def word(string):
    return string.split(' ')



class Matrix:

    def __init__(self, matrix: list[list]):
        self.matrix = matrix

    
    def to_csr(self):
        pass
    
    def to_dense(self):
        pass
        
