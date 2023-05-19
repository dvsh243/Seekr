import collections
import random
import time
import heapq
import math
from seekr.src.loss_functions import distance as Distance


class KMeans:

    def __init__(self, matrix: list, n: int, epochs: int = 4) -> None:
        self.matrix = matrix
        self.n = n  # number of centers
        print(f"\ncreating a kmeans index with {n} centers")

        self.create_centers()

        for _ in range(epochs):
            self.assign_children()
            self.compute_averages()

    

    def create_centers(self):
        self.centers = []

        for _ in range(self.n):
            choice = None
            while choice == None or choice in self.centers:
                choice = random.choice(self.matrix)
            self.centers.append(choice)
        
        # print(f"{len(self.centers)} centers created.")
    

    def assign_children(self):
        start_time = time.perf_counter()
        self.children = collections.defaultdict(list)   # {center_index : list(vector)}
        self.children_index = collections.defaultdict(list)  # {center_index : list(vector_index)}

        for vector_index, vector in enumerate(self.matrix):
            center_index = KMeans.get_closest_center(self.centers, vector)
            self.children[center_index].append(vector)
            self.children_index[center_index].append(vector_index)
        
        # print("centers' children assigned")
        print( "children sizes ->", {center_index: len(vectors) for center_index, vectors in self.children.items()} )
        print(f"children assigned in {str(time.perf_counter() - start_time)[:5]} seconds.")

        # calculating standard deviation
        avg = 0
        for center_index, vectors in self.children.items():
            avg += len(vectors) / len(self.children)

        sd = 0
        for center_index, vectors in self.children.items():
            sd += math.pow(len(vectors) - avg, 2)
        sd = math.sqrt(sd / len(self.children))

        print(f"standard deviation -> {int(sd)}", end='\n\n')


    def compute_averages(self):
        start_time = time.perf_counter()

        for center_index in self.children:
            new_center = KMeans.get_average_vector( self.matrix, self.children[center_index] )
            self.centers[center_index] = new_center
        
        print(f"new centers computed -> {str(time.perf_counter() - start_time)[:5]} seconds.")


    @staticmethod
    def get_closest_center(centers: list, vector: list) -> int:
        minHeap = []

        for center_index, center_vector in enumerate(centers):
            distance = Distance.euclidian_distance(center_vector, vector)
            heapq.heappush(minHeap, (distance, center_index))
        
        return heapq.heappop(minHeap)[1]


    @staticmethod
    def get_average_vector(matrix: list[list], vector_list: list[list]) -> list:
        dimention_avg = collections.defaultdict(int)

        for vector in vector_list:
            for dimention_id, value in vector:

                dimention_avg[dimention_id] += value
        
        result_vector = []
        for dimention_id, value in dimention_avg.items():
            result_vector.append( (
                dimention_id, 
                round(value / len(vector_list), 4)
            ) )

        # the dimentionality of the result vector is too high,
        # so we chose the closest vector to it from the given matrix
        closest_vector_index = KMeans.get_closest_center(matrix, result_vector)
        return matrix[closest_vector_index]  # closest to the average

        return result_vector  # actually the average [OPTIMIZE]