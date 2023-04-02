class TfIdfVectorizer:

    def __init__(self) -> None:
        self.features = set()
        self.corpus = ''
        self.featureMap = {}
        self.feature_matrix = []


    def fit_transform(self, corpus: list) -> None:
        self.corpus = corpus
        
        for _ in corpus:
            for feature in _.split(' '):
                self.features.add(feature)

    
    def get_feature_names(self) -> list:
        return [feature for feature in self.features]


    def get_featureMap(self) -> dict:
        return self.featureMap
    

    def create_featureMap(self) -> dict:
        feature_names = self.get_feature_names()

        featureMap, index = {}, 0
        for feature in feature_names:
            featureMap[feature] = index
            index += 1
        
        return featureMap
    

    def create_feature_matrix(self) -> None:
        # need to covert into sparse CSR matrix
        self.featureMap = self.create_featureMap()

        self.feature_matrix = [
            [0 for _ in range(len(self.featureMap))] \
                for i in range(len(self.corpus))
        ]

        for index, _ in enumerate(self.corpus):
            for feature in _.split(' '):
                self.feature_matrix[index][ self.featureMap[feature] ] += 1


    def show_feature_matrix(self) -> None:

        for i in range(len(self.feature_matrix)):

            for j in range(len(self.feature_matrix[0])):
                print(self.feature_matrix[i][j], end=' - ')
            
            print(self.corpus[i])