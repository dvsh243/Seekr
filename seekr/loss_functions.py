import math
from seekr.vectors import Vector

class distance:
    """
    Cosine Similarity. 
    Levenshtien Distance.
    Euclidean Distance. 
    Manhattan Distance. 
    Jaccard Similarity. 
    Minkowski Distance. 
    """
    
    def cosine_similarity(input1: list[list], input2: list[list]) -> float:
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
        """
        if not input1 or not input2: return 0

        target = Vector(input1)
        doc = Vector(input2)

        numerator = Vector.dot_product(target, doc)
        denominator = target.magnitude() * doc.magnitude()

        return numerator / denominator


    def euclidian_distance(input1: list[list], input2: list[list]) -> float:
        """distance = √ [(x2 – x1)^2 + (y2 – y1)^2]"""
        target = Vector(input1)
        doc = Vector(input2)
        commonFeatures = Vector.get_common_features(target, doc)

        res = 0
        for key , (n2, n1) in commonFeatures.items():
            res += math.pow(n2 - n1, 2)

        res = math.sqrt(res)
        return res
    

    def levenshtein_distance(s: str, t: str) -> int:
        return 0