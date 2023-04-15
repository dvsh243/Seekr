from seekr.utils.load_data import DB
from seekr.utils.utils import cleanDocument
from seekr.src.vectorizer import TfidfVectorizer
from seekr.utils.analyzers import whitespace, ngrams
from seekr.src.loss_functions import distance
from seekr.indexes.ann import ANN
import heapq
import time


class Seekr:

    def __init__(self) -> None:
        self.corpus: list = []
        self.totalFeatures = 0


    def load_from_db(self, location: str, column: int) -> None:
        start_time = time.perf_counter()
        
        self.db = DB(location, 5000)
        self.corpus = [cleanDocument(x[column]) for x in self.db.rows]

        self.vectorize()
        print(f"loaded {len(self.corpus)} items and vectorized in {str(time.perf_counter() - start_time)[:5]} seconds.")

        self.BTreeIndex = ANN(self.vectorizer.matrix)


    def vectorize(self) -> None:
        
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(
            corpus = self.corpus,
            analyzer = ngrams,
            skip_k = 3,
        )
        self.totalFeatures = self.vectorizer.featureIndex

    
    def __repr__(self) -> str:
        return f"<Seekr Object [{len(self.corpus)} items]>"
    

    def get_matches(self, target: str, limit: int = 3):
        target = cleanDocument(target)
        target_vector = self.vectorizer.doc_to_vector(target)

        similarity = []  # min heap

        for index, doc_vector in enumerate(self.vectorizer.matrix):
            if index % 100 == 0: print(f"compared {str((index / len(self.corpus)) * 100)[:5]} %", end='\r')

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
            res.append( (sim_value, self.db.rows[index]) )
        return res

    
    def get_indexes_matches(self, target: str, limit: int = 3):
        target = cleanDocument(target)
        target_vector = self.vectorizer.doc_to_vector(target)
        scope_matrix = self.BTreeIndex.find_leaf(target_vector)

        res = []
        for distance, index, vector in ANN.find_closest_vectors(target_vector, scope_matrix):
            res.append( (distance, self.db.rows[index]) )
        return res
