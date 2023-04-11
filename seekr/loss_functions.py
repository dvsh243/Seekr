from seekr.vectors import Vector
from seekr.vectorizer import TfidfVectorizer

class distance():
    """
    Cosine Similarity. 
    Levenshtien Distance.
    Euclidean Distance. 
    Manhattan Distance. 
    Jaccard Similarity. 
    Minkowski Distance. 
    """
    
    # def cosine_similarity(vector1: list[list], vector2: list[list]) -> float:
    #     """
    #     reference: https://www.youtube.com/watch?v=e9U0QAFbfLI

    #     x.y = |x||y|cosθ
    #     let vector(x) = 1i + 2j and vector(y) = 3i + 4j
    #     now taking dot product of x and y, 
    #     vector(x).vector(y) = (1 * 3) + (2 * 4) = 3 + 8 = 11
    #     |x| = √( 1^2 + 2^2 ) = √5
    #     |y| = √( 3^2 + 4^2 ) = √25
    #     therefore, cosθ = x.y / |x|*|y|
    #     => cosθ = 11 / √125
    #     """
    #     if not vector1 or not vector2: return 0

    #     target = Vector(vector1)
    #     doc = Vector(vector2)

    #     numerator = Vector.dot_product(target, doc)
    #     denominator = target.magnitude() * doc.magnitude()

    #     return numerator / denominator


    def euclidian_distance(vector1: list[list], vector2: list[list], dimentions: int) -> float:
        target = Vector(vector1, dimentions)
        doc = Vector(vector2, dimentions)

        return Vector.euclidian_distance(target, doc)
    

    def levenshtein_distance(s: str, t: str) -> int:
        return 0