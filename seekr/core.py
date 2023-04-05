from seekr.db import DB
from seekr.csv import CSV
from seekr.utils import cleanData, calculate_cosine_similarity
from seekr.vectorizer import TfidfVectorizer
from seekr.analyzers import whitespace, ngrams
import heapq
import time

class Seekr:

    def __init__(self) -> None:
        self.raw_corpus: list[list] = []
        self.corpus: list = []


    def load_from_db(self, location: str, column: int) -> None:
        start_time = time.perf_counter()
        db = DB(location, 10000)

        self.raw_corpus = db.getTable()
        self.corpus = cleanData( [x[column] for x in self.raw_corpus] )

        self.vectorize()
        print(f"loaded {len(self.corpus)} items and vectorized in {str(time.perf_counter() - start_time)[:5]} seconds.")


    def load_from_csv(self, location: str, column: int) -> None:
        start_time = time.perf_counter()
        csv = CSV(location, 0)

        self.raw_corpus = csv.getTable()
        self.corpus = cleanData( [x[column] for x in self.raw_corpus] )

        self.vectorize()
        print(f"loaded {len(self.corpus)} items and vectorized in {str(time.perf_counter() - start_time)[:5]} seconds.")


    def vectorize(self) -> None:
        
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(
            corpus = self.corpus,
            analyzer = ngrams
        )

    
    def __repr__(self) -> str:
        return f"<Seekr Object [{len(self.corpus)} items]>"
    

    def get_matches(self, target: str, limit: int = 10) -> list:
        
        target = target.lower()
        target_tfidf = self.vectorizer.create_target_tfidf(target)

        sim_item_heap = []  # max heap

        for i in range(len(self.corpus)):
            similarity = calculate_cosine_similarity(target_tfidf, self.tfidf_matrix[i])
            if similarity == 0: continue

            heapq.heappush(sim_item_heap, (
                similarity * -1,
                self.raw_corpus[i]
            ))

        # print(f"{len(sim_item_heap)} items in heap.")

        most_common = []
        for i in range( min(limit, len(sim_item_heap)) ):
            sim, item = heapq.heappop(sim_item_heap)
            most_common.append( (item, sim * -1) )
        
        return most_common