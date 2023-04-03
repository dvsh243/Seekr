import re


def cleanData(words: list) -> list:

    for i in range(len(words)):
        words[i] = re.sub(r'[,\'./()]|\sBD',r'', words[i])
    return words



def calculate_cosine_similarity(input1: list[list], input2: list[list]):
    doc1 = {id: tfidf_val for id, tfidf_val in input1}
    doc2 = {id: tfidf_val for id, tfidf_val in input2}

    print(doc1)
    print(doc2)

    numerator = 0
    for idx, tfidf_val in doc1.items():
        numerator += doc1
    