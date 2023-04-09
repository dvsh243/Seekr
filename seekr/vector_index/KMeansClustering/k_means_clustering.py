import random
import math
import collections
import matplotlib.pyplot as plt


class KMeansClustering:

    def __init__(self, vectors: list[list], k: int = 2) -> None:
        self.coordinates = vectors
        self.k = k

        # for pnt in self.coordinates:
            # print(' --> ', pnt)

        # plt.scatter(
        #     [x for x, y in self.coordinates],
        #     [y for x, y in self.coordinates],
        #     color = 'black'
        # )
        # plt.show()

        self.centers = self.get_random_centers()
        self.create_clusters()

        # colors = ['red', 'blue', 'green']
        # for i, (cluster, points) in enumerate(self.clusterList.items()):
        #     plt.scatter(
        #         [x for x, y in points],
        #         [y for x, y in points],
        #         color = colors[i]
        #     )
        # plt.show()



    def get_random_centers(self) -> list:
        centers = []

        for i in range(self.k):
            point = random.choice(self.coordinates)
            while point in centers: point = random.choice(self.coordinates)
            centers.append(point)

        return centers

    
    def euclidian_distance(self, p1: tuple, p2: tuple):
        """distance = √ [ (x2 - x1)^2 + (y2 - y1)^2 ]"""
        res = 0
        for n1, n2 in zip(p1, p2):
            res += math.pow(n2 - n1, 2)

        return math.sqrt(res)


    def get_cluster(self, target: tuple):
        """which cluster does this point belong to"""
        res = (None, float('inf'))  # (center, distance)
    
        for center in self.centers:
            distance = self.euclidian_distance(center, target)
            if distance < res[1]:
                res = (center, distance)
        
        return res


    def create_clusters(self):
        self.clusterIndex = {}  # map {point : center of its cluster}
        self.clusterList = collections.defaultdict(list)  # {cluster_center : [(point, distance_from_center) that lie in the cluster]}

        for point in self.coordinates:
            cluster_center, distance_from_center = self.get_cluster(point)

            self.clusterIndex[ tuple(point) ] = tuple(cluster_center)
            self.clusterList[ tuple(cluster_center) ].append( point )

            # print(f"point {point} belongs to cluster -> {cluster_center} \t [distance: {distance_from_center}]")

    
    def get_cluster_means(self) -> None:
        self.clusterMean = {}

        for cluster, points in self.clusterList.items():
            # print(cluster, points, sep=' --> ')

            mean = []
            for n in range(len(points[0])):
            
                nSum = 0
                for point in points:
                    nSum += point[n] 
                    # print(point[n], end=' - ')
                # print(nSum)

                mean.append(nSum / len(points))

            self.clusterMean[ tuple(cluster) ] = tuple(mean)



if __name__ == '__main__':
    coordinates = [
        (1, 3, 0), (2, 2, 0), (2, 4, 1), (3, 3, 1), (4, 4, 0),
        (7, 4, 0), (7, 5, 0), (8, 4, 1), (9, 3, 1), (8, 3, 0)
    ]
    KMeansClustering(vectors = coordinates, k = 2)
