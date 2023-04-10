from seekr.load_data import DB, CSV
from seekr.utils import cleanData
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
        
        db = DB(location, 10)
        self.corpus = [cleanData(x[column]) for x in db.rows]

        self.vectorize()

        print(f"\nloaded {len(self.corpus)} items and vectorized in {str(time.perf_counter() - start_time)[:5]} seconds.")


    def vectorize(self) -> None:
        
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(
            corpus = self.corpus,
            analyzer = whitespace
        )

    
    def __repr__(self) -> str:
        return f"<Seekr Object [{len(self.corpus)} items]>"
