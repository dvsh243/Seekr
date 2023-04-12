import json
import math
import random


class TreeNode:
    
    def __init__(self, vector: list[tuple] = None) -> None:
        self.vector = vector
        self.left = None
        self.right = None 
    
    def __repr__(self) -> str:
        return f"<TreeNode: [{self.vector}]>"
    


class ANN:

    def __init__(self) -> None:
        self.root = TreeNode()

        with open('seekr/indexes/test_vectors.json') as f:
            self.matrix = json.load(f)

        self.create_index()


    def create_index(self):
        
        for center in self.create_random_centers():
            print(f"center ---> {center[:3]}...")


    def create_random_centers(self, N: int  = 2) -> list:
        centers = [random.choice(self.matrix) for _ in range(N)]
        # print("choosing 2 random centers.")
        # for vector in centers: print("vector -> ", vector[:4], "...")

        center_count = [0 for _ in range(N)]

        for vector in self.matrix:
            center_index, distance = ANN.get_closest_center(centers, vector)
            center_count[center_index] += 1
        
        print("random centers created")
        print("no. of vectors in centers ->", center_count)

        return centers



    @staticmethod
    def get_closest_center(centers: list[list], vector: list):
        """which center is this vector closer to"""
        closer = (None, float('inf'))  # (center_index, distance) pair

        for center_index, center_vector in enumerate(centers):
            distance = ANN.actual_euclidian_distance(center_vector, vector)
            if distance < closer[1]:
                closer = (center_index, distance)

        return closer
    

    @staticmethod
    def actual_euclidian_distance(vector1, vector2) -> float:
        """
        vector1 -> [(3, 0.53612), (7, 1.518630)]
        vector2 -> [(0, 0.910361), (7, 2.11983), (9, 0.21591), (14, 1.85192)]
        common = {0: (0, 0.910361), 3: (0.53612, 0), 7: (1.518630, 2.11983) ...}
        """
        vector1_map = {index: value for index, value in vector1}
        vector2_map = {index: value for index, value in vector2}
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
    

if __name__ == '__main__':
    ANN()