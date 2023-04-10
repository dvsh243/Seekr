from gensim.models import KeyedVectors
import numpy as np

class GensimIndex:

    def __init__(self, vectors: list[list], k: int = 20) -> None:
        self.model = KeyedVectors(len(vectors[0]))
        self.model.add_vectors( [i for i in range(len(vectors))], vectors )

        print("vector model created.", self.model)


    def match(self, target_tfidf_dense: list):

        neighbors = self.model.most_similar(
            np.array(target_tfidf_dense, dtype=np.float32),
            topn=5
        )
        return neighbors