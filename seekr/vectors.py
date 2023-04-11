import math

class Vector:

    def __init__(self, array: list[tuple], dimentions: int) -> None:
        self.values = array

    # wont work on sparse vectors
    # def magnitude(self) -> float:
    #     mag = 0
    #     for value in self.values:
    #         mag += math.pow(value, 2)

    #     return math.sqrt(mag)


    # wont work on sparse vectors
    # @staticmethod
    # def dot_product(vector1, vector2) -> float:
    #     dot = 0
    #     for i1, i2 in zip(vector1.values, vector2.values):
    #         dot += i1 * i2

    #     return dot


    @staticmethod
    def dense_euclidian_distance(vector1, vector2) -> float:
        """distance = √ [(x2 - x1)^2 + (y2 - y1)^2]"""
        dist = 0
        for x1, x2 in zip(vector1.values, vector2.values):
            if x1 == 0 and x2 == 0: continue  # [OPTIMIZE] optimizes comparing (by alot)
            dist += math.pow(x2 - x1, 2)
        
        return math.sqrt(dist)

    
    @staticmethod
    def sparse_euclidian_distance(vector1, vector2) -> float:
        dist = 0
        doc_indexToValue = {index: value for index, value in vector2.values}

        for index, value in vector1.values:
            dist += math.pow(value - doc_indexToValue.get(index, 0), 2)
        
        return math.sqrt(dist)
     
    
    def __repr__(self) -> str:
        return f"<Vector: {self.values}>"
    
