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
    def euclidian_distance(vector1, vector2) -> float:
        dist = 0
        doc_indexToValue = {index: value for index, value in vector2.values}

        for index, value in vector1.values:
            dist += math.pow(value - doc_indexToValue.get(index, 0), 2)
        
        return math.sqrt(dist)
    

    @staticmethod
    def actual_euclidian_distance(vector1, vector2) -> float:
        """
        vector1 -> [(3, 0.53612), (7, 1.518630)]
        vector2 -> [(0, 0.910361), (7, 2.11983), (9, 0.21591), (14, 1.85192)]
        common = {0: (0, 0.910361), 3: (0.53612, 0), 7: (1.518630, 2.11983) ...}
        """
        vector1_map = {index: value for index, value in vector1.values}
        vector2_map = {index: value for index, value in vector2.values}
        common = {}

        for index, value in vector1_map.items():
            common[index] = (value, vector2_map.get(index, 0))

        for index, value in vector2_map.items():
            if index not in common:
                common[index] = (0, value)

        dist = 0
        for _, (value1, value2) in common.items():
            dist += math.pow(value2 - value1, 2)

        return math.sqrt(dist)
    
     
    
    def __repr__(self) -> str:
        return f"<Vector: {self.values}>"
    
