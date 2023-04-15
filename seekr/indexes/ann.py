import json
import math
import random
import collections
import time
import heapq


class TreeNode:
    
    def __init__(self, vector: list = None, leaf_vectors: list = [], is_leaf: bool = False) -> None:
        self.vector = vector
        self.leaf_vectors = leaf_vectors  # only populate for leaf nodes

        self.left = None
        self.right = None 
        self.is_leaf = is_leaf
    
    def __repr__(self) -> str:
        return f"<TreeNode: {self.vector[:3]}...>" if self.vector else f"<TreeNode: ROOT>"
    


class ANN:

    def __init__(self, matrix: list) -> None:
        self.root = TreeNode()
        self.matrix = matrix
        self.minimumLeafCount = 500  # number of vectors the leaf node in the index tree will hold
        
        self.create_index()


    def create_index(self):
        print(f"creating index of {len(self.matrix)} vectors.")
        start_time = time.perf_counter()
        
        root_centers, children_indexes = self.create_random_centers(self.matrix)
        
        self.root = TreeNode()
        self.root.left = self.populate_tree(root_centers[0], children_indexes[0])
        self.root.right = self.populate_tree(root_centers[1], children_indexes[1])

        # print("self.root.left", self.root.left); print("self.root.right", self.root.right)

        print(f"index created in {str(time.perf_counter() - start_time)[:5]} seconds.")



    def populate_tree(self, center_vector: list, children_indexes: list[int], depth = 0) -> TreeNode:
        # print(f"\n[{depth}] populate tree func() called.")
        scope_matrix = [self.matrix[i] for i in children_indexes]

        # base case
        if len(scope_matrix) < self.minimumLeafCount:
            # print(f"base case reached [{len(scope_matrix)} vectors].")
            return TreeNode(vector = center_vector, leaf_vectors = scope_matrix, is_leaf = True)
        
        # else, split into 2 centers
        centers, scope_children_indexes = self.create_random_centers(scope_matrix)

        node = TreeNode(vector = center_vector)
        node.left = self.populate_tree(centers[0], scope_children_indexes[0], depth + 1)
        node.right = self.populate_tree(centers[1], scope_children_indexes[1], depth + 1)

        return node




    def create_random_centers(self, matrix: list, N: int  = 2) -> tuple[list, dict]:
        centers = [random.choice(matrix) for _ in range(N)]

        center_count = [0 for _ in range(N)]
        children_indexes = collections.defaultdict(list)

        for i, vector in enumerate(matrix):
            center_index, distance = ANN.get_closest_center(centers, vector)
            center_count[center_index] += 1
            children_indexes[center_index].append(i)
        
        # print("random centers created.")
        # print("no. of vectors in centers ->", center_count)

        return centers, children_indexes



    def find_leaf(self, target_vector: list) -> TreeNode:
        depth = 0
        node = self.root

        # print(f"searching for target_vector -> {target_vector[:4]}")
        
        while node:
            if node.is_leaf: return node.leaf_vectors

            if (
                ANN.actual_euclidian_distance(node.left.vector, target_vector) < \
                ANN.actual_euclidian_distance(node.right.vector, target_vector)
            ):
                # print("go left", depth)
                node = node.left
        
            else:
                # print("go right", depth)
                node = node.right
            
            depth += 1
                



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
    

    @staticmethod
    def find_closest_vectors(target_vector: list, scope_matrix: list, N: int = 3) -> list:

        minHeap = []

        for index, vector in enumerate(scope_matrix):
            distance = ANN.actual_euclidian_distance(target_vector, vector)
            heapq.heappush(minHeap, (distance, index, vector))

        closest = []
        for i in range(N):
            distance, index, vector = heapq.heappop(minHeap)
            closest.append( (distance, index, vector) )
        
        return closest

'''
if __name__ == '__main__':
    
    with open('seekr/indexes/test_vectors.json') as f:
        matrix = json.load(f)

    index = ANN(matrix[:3000])
    leaf_vectors = index.find_leaf(matrix[159])

    # print(f"need to compare to {len(leaf_vectors)} leaf_vectors.")
    # print(f"example leaf_vector -> {leaf_vectors[0]}")



    print("closest vectors by exhaustive search :-")
    start_time = time.perf_counter()
    ANN.find_closest_vectors(target_vector = matrix[159], scope_matrix = matrix)
    print(f"index created in {str(time.perf_counter() - start_time)[:5]} seconds.")


    print("closest vectors by indexed search :-")
    start_time = time.perf_counter()
    ANN.find_closest_vectors(target_vector = matrix[159], scope_matrix = leaf_vectors)
    print(f"index created in {str(time.perf_counter() - start_time)[:5]} seconds.")

'''