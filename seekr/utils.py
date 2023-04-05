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

    x.y = |x||y|cosθ
    let vector(x) = 1i + 2j and vector(y) = 3i + 4j
    now taking dot product of x and y, 
    vector(x).vector(y) = (1 * 3) + (2 * 4) = 3 + 8 = 11
    |x| = √( 1^2 + 2^2 ) = √5
    |y| = √( 3^2 + 4^2 ) = √25
    therefore, cosθ = x.y / |x|*|y|
    => cosθ = 11 / √125

    - # - # - # - # - # - # - # - # - #   
    features ->      32    33    29
    doc_tfidf ->      a     b     c
    target_tfidf ->   d     e     f

    numerator = (a * d) + (b * e) + (c * f)
    denominator = sqrt( (a^2 + b^2 + c^2) * (d^2 + e^2 + f^2) )
    """
    # find a more optimized code

    doc1 = {idx: tfidf for idx, tfidf in input1 if idx != -1}
    # if idx = -1, means it will not ecist in the second string => 0 impact on cosine similarity
    doc2 = {idx: tfidf for idx, tfidf in input2}

    commonFeatures = {}
    for idx, tfidf in doc1.items():
        if idx in doc2: commonFeatures[idx] = (tfidf, doc2[idx])  # (target_tfidf, doc_tfidf)
    # print("commonFeatures", commonFeatures)
    if not commonFeatures: return 0

    # iterating over feature idx
    # vector dot product of target and document vectors,
    # [target(i) * doc(i)] + [target(j) * doc(j)] + [target(k) * doc(k)] 
    numerator = 0
    for idx, (target_tfidf, doc_tfidf) in commonFeatures.items():
        numerator += target_tfidf * doc_tfidf
    # print("numerator", numerator, end='\n\n')
    
    # iterating over tfidf values of target then of document 
    # adding magnitude of target vector and of document vector
    denominator = None
    tmp_target, tmp_doc = 0, 0
    for target_tfidf, doc_tfidf in list(commonFeatures.values()):
        tmp_target += math.pow(target_tfidf, 2)
        tmp_doc += math.pow(doc_tfidf, 2)
    
    denominator = math.sqrt(tmp_target + tmp_doc)
    # print("denominator", denominator)

    return numerator / denominator
