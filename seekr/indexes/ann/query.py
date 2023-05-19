from seekr.indexes.ann.ann import ANN
from seekr.src.loss_functions import distance as Distance
import heapq


class ANNQuery(ANN):

    def __init__(self, matrix: list, min_leaf_count: int = 1000) -> None:
        super().__init__(matrix, min_leaf_count, sensitivity=0.70, forest_size=1)


    def find_leaf(self, target_vector: list) -> list:
        depth = 0
        leaf_indexes = []

        for i in range(len(self.roots)):
            node = self.roots[i]

            # print(f"searching for target_vector -> {target_vector[:4]}")

            while node:
                if node.is_leaf: 
                    leaf_indexes.extend( node.leaf_indexes )
                    break

                if (
                    Distance.euclidian_distance(node.left.vector, target_vector) < \
                    Distance.euclidian_distance(node.right.vector, target_vector)
                ): node = node.left
                else: node = node.right

                depth += 1
        
        return list(set(leaf_indexes))  # multiple leaf nodes of different trees can hold same index

    
    def find_closest_vectors(self, target_vector: list, leaf_indexes: list, N: int = 3) -> list:

        scope_matrix = [self.matrix[i] for i in leaf_indexes]
        minHeap = []

        for index, vector in zip(leaf_indexes, scope_matrix):
            distance = Distance.euclidian_distance(target_vector, vector)
            heapq.heappush(minHeap, (distance, index, vector))

        closest = []
        for i in range( min(N, len(minHeap)) ):
            distance, index, vector = heapq.heappop(minHeap)
            closest.append( (distance, index, vector) )
        
        return closest

    