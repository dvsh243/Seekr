from seekr.indexes.kmeans.kmeans import KMeans
from seekr.src.loss_functions import distance as Distance
import heapq


class KMeansQuery(KMeans):

    def __init__(self, matrix: list, n: int = 10, epochs: int = 2) -> None:
        super().__init__(matrix, n, epochs)

    
    def find_closest_vectors(self, target_vector: list, N: int = 3) -> list:
        
        minHeap = []
        for center_index, center_vector in enumerate(self.centers):
            distance = Distance.euclidian_distance(center_vector, target_vector)
            heapq.heappush( minHeap, (distance, center_index) )

        center_index = heapq.heappop(minHeap)[1]  # search in this cluster
        minHeap = []
        for vector_index in self.children_index[center_index]:
            distance = Distance.euclidian_distance(self.matrix[vector_index], target_vector)
            heapq.heappush( minHeap, (distance, vector_index) )

        closest = []
        for i in range( min(N, len(minHeap)) ):
            distance, index = heapq.heappop(minHeap)
            closest.append( (distance, index) )
        
        return closest
        