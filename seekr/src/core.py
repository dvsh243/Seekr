from seekr.utils.load_data import DB
from seekr.utils.utils import cleanDocument
from seekr.src.vectorizer import TfidfVectorizer
from seekr.utils.analyzers import whitespace, ngrams
from seekr.src.loss_functions import distance
from seekr.index.query import ANNQuery
import heapq
import time


class Seekr:

    def __init__(self) -> None:
        self.corpus: list = []
        self.totalFeatures = 0


    def load_from_db(self, location: str, column: int) -> None:
        start_time = time.perf_counter()
        
        self.db = DB(location, 5000)
        # self.corpus = [cleanDocument(x[column]) for x in self.db.rows]

        for x in self.db.rows:
            if len(x[column]) < 3: continue
            self.corpus.append( cleanDocument(x[column]) )

        self.vectorize()
        print(f"loaded {len(self.corpus)} items and vectorized in {str(time.perf_counter() - start_time)[:5]} seconds.")

        self.BTreeIndex = ANNQuery(self.vectorizer.matrix, 1000)

    
    def load_from_array(self, input_array: list) -> None:
        start_time = time.perf_counter()

        for x in input_array:
            self.corpus.append( cleanDocument(x) )

        self.vectorize()
        print(f"loaded {len(self.corpus)} items and vectorized in {str(time.perf_counter() - start_time)[:5]} seconds.")
        self.BTreeIndex = ANNQuery(self.vectorizer.matrix, 100)


    def vectorize(self) -> None:
        
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(
            corpus = self.corpus,
            analyzer = ngrams,
            skip_k = 0,
        )
        self.totalFeatures = self.vectorizer.featureIndex

    
    def __repr__(self) -> str:
        return f"<Seekr Object [{len(self.corpus)} items]>"
    

    def get_matches(self, target: str, limit: int = 3):
        target = cleanDocument(target)
        target_vector = self.vectorizer.doc_to_vector(target)

        similarity = []  # min heap

        for index, doc_vector in enumerate(self.vectorizer.matrix):
            # if index % 100 == 0: print(f"compared {str((index / len(self.corpus)) * 100)[:5]} %", end='\r')

            heapq.heappush(
                similarity,
                ( distance.euclidian_distance(
                        vector1 = target_vector, 
                        vector2 = doc_vector, 
                        dimentions = self.totalFeatures,
                    ), 
                    index 
                )
            )

        res = []
        for _ in range( min(len(similarity), limit) ):
            sim_value, index = heapq.heappop(similarity)
            res.append( (sim_value, self.corpus[index]) )
        return res

    
    def get_indexes_matches(self, target: str, limit: int = 3):
        target = cleanDocument(target)
        target_vector = self.vectorizer.doc_to_vector(target)
        leaf_indexes = self.BTreeIndex.find_leaf(target_vector)
        # print(f"found {len(leaf_indexes)} vectors to search.\nleaf_indexes -> {leaf_indexes[:5]}")

        res = []
        for distance, index, vector in self.BTreeIndex.find_closest_vectors(target_vector, leaf_indexes):
            res.append( (distance, self.corpus[index]) )
        return res
