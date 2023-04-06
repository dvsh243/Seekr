import math

class Vector:

    def __init__(self, array: list) -> None:
        self.raw_array = array
        self.featureMap = {idx: tfidf for idx, tfidf in array}
    
    def magnitude(self) -> float:
        mag = 0
        for idx, tfidf in self.raw_array:
            mag += math.pow(tfidf, 2)
        return math.sqrt(mag)

    def __repr__(self) -> str:
        return f"<Vector: {self.raw_array}>"
    


def dot_product(vector1: Vector, vector2: Vector) -> float:
    dot = 0

    for idx, val in vector1.featureMap.items():
        if idx in vector2.featureMap:
            dot += val * vector2.featureMap[idx]
    
    return dot