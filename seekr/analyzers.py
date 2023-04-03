


def whitespace(document: str) -> list:
    return document.split(' ')


def ngrams(document: str, n: int = 3) -> list:
    ngram_list = []
    for i in range(2, len(document)):
        ngram_list.append( document[i - 2: i + 1] )
    return ngram_list