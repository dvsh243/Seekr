import json
import random
import math
import collections

with open('seekr/indexes/test_vectors.json') as f:
    matrix = json.load(f)



def euclidian_distance(vector1, vector2) -> float:
    dist = 0
    doc_indexToValue = {index: value for index, value in vector2}

    for index, value in vector1:
        dist += math.pow(value - doc_indexToValue.get(index, 0), 2)
    
    return math.sqrt(dist)


def get_center(centers: list[list], vector: list):
    """which center is this vector closer to"""
    closer = (None, float('inf'))  # (center_index, distance) pair
    
    for center_index, center_vector in enumerate(centers):
        distance = euclidian_distance(center_vector, vector)
        if distance < closer[1]:
            closer = (center_index, distance)
    
    return closer




for _ in range(20):

    N = 2
    centers = [random.choice(matrix) for _ in range(N)]
    # print("choosing 2 random centers.")
    # for vector in centers: print("vector -> ", vector[:4], "...")

    center_count = [0 for _ in range(N)]
    
    for vector in matrix:
        center_index, distance = get_center(centers, vector)
        center_count[center_index] += 1

    print(center_count)






















''' PASTE THIS CODE IN `core.py` to populate `test_vectors.json`
test_vectors = []
for vector in self.vectorizer.matrix:
    test_vectors.append(vector)
import json
with open('seekr/indexes/test_vectors.json', 'w') as f:
    json.dump(test_vectors, f)
print("data written in json file.")
'''