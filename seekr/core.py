from seekr.load_data import DB, CSV
from seekr.utils import cleanDocument
from seekr.vectorizer import TfidfVectorizer
from seekr.analyzers import whitespace, ngrams
from seekr.loss_functions import distance
import heapq
import time


class Seekr:

    def __init__(self) -> None:
        self.corpus: list = []


    def load_from_db(self, location: str, column: int) -> None:
        start_time = time.perf_counter()
        
        self.db = DB(location, 20)
        self.corpus = [cleanDocument(x[column]) for x in self.db.rows]

        self.vectorize()

        print(f"\nloaded {len(self.corpus)} items and vectorized in {str(time.perf_counter() - start_time)[:5]} seconds.")


    def vectorize(self) -> None:
        
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(
            corpus = self.corpus,
            analyzer = ngrams
        )

    
    def __repr__(self) -> str:
        return f"<Seekr Object [{len(self.corpus)} items]>"
    

    def get_matches(self, target: str, limit: int = 3):
        target = cleanDocument(target)
        target_vector = self.vectorizer.doc_to_vector(target)

        similarity = []  # min heap

        for index, doc_vector in enumerate(self.vectorizer.matrix):
            heapq.heappush(
                similarity,
                ( distance.euclidian_distance(target_vector, doc_vector), index )
            )

        res = []
        for i in range(limit):
            sim_value, index = heapq.heappop(similarity)
            res.append( (sim_value, self.db.rows[index]) )
        return res