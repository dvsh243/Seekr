import math
import random
import collections
import time
from seekr.src.loss_functions import distance as Distance


class TreeNode:
    
    def __init__(self, vector: list = None, leaf_indexes: list = [], is_leaf: bool = False) -> None:
        self.vector = vector
        self.leaf_indexes = leaf_indexes  # only populate for leaf nodes

        self.left = None
        self.right = None 
        self.is_leaf = is_leaf
    
    def __repr__(self) -> str:
        return f"<TreeNode: {self.vector[:3]}...>" if self.vector else f"<TreeNode: ROOT>"
    


class ANN:

    def __init__(self, matrix: list, min_leaf_count: int = 2000) -> None:
        self.root = TreeNode()
        self.matrix = matrix
        self.minimumLeafCount = min_leaf_count  # number of vectors the leaf node in the index tree will hold
        
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
            return TreeNode(vector = center_vector, leaf_indexes = children_indexes, is_leaf = True)
        
        # else, split into 2 centers
        centers, scope_children_indexes = self.create_random_centers(scope_matrix)

        node = TreeNode(vector = center_vector)
        node.left = self.populate_tree(centers[0], scope_children_indexes[0], depth + 1)
        node.right = self.populate_tree(centers[1], scope_children_indexes[1], depth + 1)

        return node


    def create_random_centers(self, matrix: list) -> tuple[list, dict]:
        center_count = [0, 0]
        centers = []
        children_indexes = {}
        
        def go():
            nonlocal centers, children_indexes, center_count
            centers = [random.choice(matrix) for _ in range(2)]
            center_count = [0, 0]

            children_indexes = collections.defaultdict(list)

            for i, vector in enumerate(matrix):
                center_index, distance = ANN.get_closest_center(centers, vector)
                center_count[center_index] += 1
                children_indexes[center_index].append(i)
        
        go()
        count = 0
        while sum(center_count) / 8 > min(center_count):  # find a better way?
            go()  # for dividing vectors equally
            count += 1

        # print("random centers created.")
        print(f"clustered vectors -> {center_count} \t [re ran {count} times]")

        return centers, children_indexes


    @staticmethod
    def get_closest_center(centers: list[list], vector: list):
        """which center is this vector closer to"""
        closer = (None, float('inf'))  # (center_index, distance) pair

        for center_index, center_vector in enumerate(centers):
            distance = Distance.euclidian_distance(center_vector, vector)
            if distance < closer[1]:
                closer = (center_index, distance)

        return closer
