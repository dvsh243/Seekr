import re
import math

def cleanData(words: list) -> list:

    for i in range(len(words)):
        words[i] = re.sub(r'[,\'./()]|\sBD',r'', words[i])
        words[i] = words[i].lower()
    return words



def calculate_cosine_similarity(input1: list[list], input2: list[list]):
    """
    reference: https://www.youtube.com/watch?v=e9U0QAFbfLI

    
    features ->      32    33    29
    doc_tfidf ->      a     b     c
    target_tfidf ->   d     e     

    numerator = (a * d) + (b * e) + (c * f)
    denominator = sqrt( (a^2 + b^2 + c^2) * (d^2 + e^2 + f^2) )
    """
    # FIX DENOMINATOR ASAP, WRONG MATH

    doc1 = {idx: tfidf for idx, tfidf in input1 if idx != -1}
    # if idx = -1, means it will not ecist in the second string => 0 impact on cosine similarity
    doc2 = {idx: tfidf for idx, tfidf in input2}

    commonFeatures = {}
    for idx, tfidf in doc1.items():
        if idx in doc2: commonFeatures[idx] = (tfidf, doc2[idx])  # (target_tfidf, doc_tfidf)
    # print("commonFeatures", commonFeatures)
    if not commonFeatures: return 0

    # iterating over feature idx
    numerator = 0
    for idx, (target_tfidf, doc_tfidf) in commonFeatures.items():
        numerator += target_tfidf * doc_tfidf
    # print("numerator", numerator, end='\n\n')
    
    # iterating over tfidf values of target then of document
    denominator = None
    tmp_target, tmp_doc = 0, 0
    for target_tfidf, doc_tfidf in list(commonFeatures.values()):
        tmp_target += math.pow(target_tfidf, 2)
        tmp_doc += math.pow(doc_tfidf, 2)
    
    denominator = math.sqrt(tmp_target + tmp_doc)
    # print("denominator", denominator)

    return numerator / denominator
