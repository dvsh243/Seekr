from seekr.utils.load_data import DB
from seekr.utils.utils import cleanDocument
from seekr.src.vectorizer import TfidfVectorizer
from seekr.utils.analyzers import whitespace, ngrams
from seekr.index.query import ANNQuery
import time
from seekr.src.query import Query


class Seekr:

    def __init__(self) -> None:
        self.corpus: list = []
        self.totalFeatures = 0


    def load_from_db(self, db_name: str, location: str, column: int) -> None:
        start_time = time.perf_counter()
        
        self.db = DB(db_name, location, 5000)
        # self.corpus = [cleanDocument(x[column]) for x in self.db.rows]

        for x in self.db.rows:
            if len(x[column]) < 3: continue
            self.corpus.append( cleanDocument(x[column]) )

        self.vectorize()
        print(f"loaded {len(self.corpus)} items and vectorized in {str(time.perf_counter() - start_time)[:5]} seconds.")

        self.BTreeIndex = ANNQuery(
            self.vectorizer.matrix, 
        )
        

    def vectorize(self) -> None:
        
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(
            corpus = self.corpus,
            analyzer = whitespace,
            skip_k = 0,
        )
        self.totalFeatures = self.vectorizer.featureIndex

    
    def query(self, target: str, limit: int = 3, index_type: str = 'linear'):
        query = Query(
                self.corpus, 
                self.vectorizer, 
                self.BTreeIndex, 
                self.totalFeatures, 
                limit
            )
        
        return query.query(
                target, 
                index_type = index_type
            )

    
    def __repr__(self) -> str:
        return f"<Seekr Object [{len(self.corpus)} items]>"