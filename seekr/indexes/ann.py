import json
import math
import random
import collections


class TreeNode:
    
    def __init__(self, vector: list = None, leaf_vectors: list = []) -> None:
        self.vector = vector
        self.leaf_vectors = leaf_vectors  # only populate for leaf nodes

        self.left = None
        self.right = None 
    
    def __repr__(self) -> str:
        return f"<TreeNode: {self.vector[:3]}...>" if self.vector else f"<TreeNode: ROOT>"
    


class ANN:

    def __init__(self, matrix: list) -> None:
        self.root = TreeNode()
        self.matrix = matrix
        
        self.create_index()


    def create_index(self):
        
        root_centers, children_indexes = self.create_random_centers(self.matrix)

        self.root = TreeNode()
        self.root.left = TreeNode(root_centers[0])
        self.root.right = TreeNode(root_centers[1])

        print("root", self.root); print("root left", self.root.left); print("root right", self.root.right, end='\n\n')

        print("populating root.left")
        self.populate_tree(
            self.root.left, 
            children_indexes[0]
        )

        print("populating root.right")
        self.populate_tree(
            self.root.right, 
            children_indexes[1]
        )


    def populate_tree(self, node: TreeNode, children_indexes: list[int]):
        print("\npopulate tree func() called.")

        scope_matrix = [self.matrix[i] for i in children_indexes]

        # base case
        if len(scope_matrix) < 2000:
            print(f"[{len(scope_matrix)} vectors] base case reached.")
            return TreeNode(node, leaf_vectors = scope_matrix)
        
        # else, split into 2 centers
        centers, scope_children_indexes = self.create_random_centers(scope_matrix)






    # def populate_tree(self, node: TreeNode, children_indexes: list[int]):
    #     print("\npopulate tree func() called.")
        
    #     # list of all the vectors which were closer to this center vector
    #     scope_matrix = [self.matrix[i] for i in children_indexes]

    #     # base case
    #     if len(scope_matrix) < 2000:
    #         print(f"[{len(scope_matrix)} vectors] base case reached.")
    #         return TreeNode(node, leaf_vectors = scope_matrix)
    
    #     # else, recalculate centers in the scope matrix
    #     centers, scope_children_indexes = self.create_random_centers(scope_matrix)
        
    #     node.left = TreeNode(centers[0])
    #     print("calling on left.")
    #     self.populate_tree(node.left, scope_children_indexes[0])

    #     node.right = TreeNode(centers[1])
    #     print("calling on right.")
    #     self.populate_tree(node.right, scope_children_indexes[0])



    def create_random_centers(self, matrix: list, N: int  = 2) -> tuple[list, dict]:
        centers = [random.choice(matrix) for _ in range(N)]

        center_count = [0 for _ in range(N)]
        children_indexes = collections.defaultdict(list)

        for i, vector in enumerate(matrix):
            center_index, distance = ANN.get_closest_center(centers, vector)
            center_count[center_index] += 1
            children_indexes[center_index].append(i)
        
        print("random centers created.")
        print("no. of vectors in centers ->", center_count)

        return centers, children_indexes



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
    
    with open('seekr/indexes/test_vectors.json') as f:
        matrix = json.load(f)
    ANN(matrix)
