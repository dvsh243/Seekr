from seekr.db import DB
from seekr.utils import cleanData, calculate_cosine_similarity
from seekr.vectorizer import TfidfVectorizer
from seekr.analyzers import whitespace, ngrams


class Seekr:

    def __init__(self, location: str) -> None:
        db = DB(location, 10000)
        
        self.corpus = cleanData( db.getWords() )
        self.tfidf_matrix = self.vectorize(self.corpus)


    def vectorize(self, corpus: list) -> list[list[int, float]]:
        
        self.vectorizer = TfidfVectorizer()
        tfidf_matrix = self.vectorizer.fit_transform(
            corpus = corpus,
            analyzer = whitespace
        )

        return tfidf_matrix
    
    
    def __repr__(self) -> str:
        return "<Seekr Object>"
    

    def get_matches(self, target: str) -> list:
        
        print("target ->", target)
        tfidf_list = self.vectorizer.create_target_tfidf(target)

        print(self.vectorizer.analyze(target))
        print(tfidf_list) 