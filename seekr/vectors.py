import math

class Vector:

    def __init__(self, array: list[tuple], dimentions: int, is_sparse: bool = True) -> None:
        """
        array: list[tuple], is a sparse vector datastructure
        """
        # converting sprase vector to dense vector

        if is_sparse:
            self.values = [0 for _ in range(dimentions)]
            for index, value in array:
                self.values[index] = value
        
        else:
            self.values = array
    
    
    def magnitude(self) -> float:
        mag = 0
        for value in self.values:
            mag += math.pow(value, 2)

        return math.sqrt(mag)


    @staticmethod
    def dot_product(vector1, vector2) -> float:
        dot = 0
        for i1, i2 in zip(vector1.values, vector2.values):
            dot += i1 * i2

        return dot


    @staticmethod
    def euclidian_distance(vector1, vector2) -> float:
        """distance = √ [(x2 - x1)^2 + (y2 - y1)^2]"""
        dist = 0
        for x1, x2 in zip(vector1.values, vector2.values):
            if x1 == 0 and x2 == 0: continue  # [OPTIMIZE] optimizes comparing (by alot)
            dist += math.pow(x2 - x1, 2)
        
        return math.sqrt(dist)

    
    def __repr__(self) -> str:
        return f"<Vector: {self.values[:3]}... {len(self.values)}>"
    
