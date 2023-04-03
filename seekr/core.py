from seekr.db import DB
from seekr.utils import cleanData
from seekr.vectorizer import TfidfVectorizer
from seekr.analyzers import whitespace, ngrams


class Seekr:

    def __init__(self, location: str) -> None:
        db = DB(location, 10000)
        
        self.corpus = cleanData( db.getWords() )
        self.tfidf_matrix = self.vectorize(self.corpus)


    def vectorize(self, corpus: list) -> list[list[int, float]]:
        
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(
            corpus = corpus,
            analyzer = whitespace
        )


        for i in range(len(tfidf_matrix)):
            if i > 10: break

            print(vectorizer.analyze(corpus[i]))
            print(tfidf_matrix[i], end='\n\n')
        
        target = '!J'
        count = 0
        for doc in self.corpus:
            for feature in vectorizer.analyze(doc):
                if feature == target: count += 1; break
        print(f"feature '{target}' can be found in {count} / {len(self.corpus)} documents")

        return tfidf_matrix