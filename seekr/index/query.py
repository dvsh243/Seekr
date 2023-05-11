from seekr.index.ann import ANN
from seekr.src.loss_functions import distance as Distance
import heapq


class ANNQuery(ANN):

    def __init__(self, matrix: list, min_leaf_count: int = 2000) -> None:
        super().__init__(matrix, min_leaf_count)


    def find_leaf(self, target_vector: list) -> list:
        depth = 0
        node = self.root

        # print(f"searching for target_vector -> {target_vector[:4]}")
        
        while node:
            if node.is_leaf: return node.leaf_indexes

            if (
                Distance.euclidian_distance(node.left.vector, target_vector) < \
                Distance.euclidian_distance(node.right.vector, target_vector)
            ):
                # print("go left", depth)
                node = node.left
        
            else:
                # print("go right", depth)
                node = node.right
            
            depth += 1
    

    
    def find_closest_vectors(self, target_vector: list, leaf_indexes: list, N: int = 3) -> list:

        scope_matrix = [self.matrix[i] for i in leaf_indexes]
        minHeap = []

        for index, vector in zip(leaf_indexes, scope_matrix):  # wrong index!!
            distance = Distance.euclidian_distance(target_vector, vector)
            heapq.heappush(minHeap, (distance, index, vector))

        closest = []
        for i in range( min(N, len(minHeap)) ):
            distance, index, vector = heapq.heappop(minHeap)
            closest.append( (distance, index, vector) )
        
        return closest

    