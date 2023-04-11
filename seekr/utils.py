import re

def cleanDocument(document: str) -> str:
    document = document.lower()
    return re.sub(r'[,\'./()]|\sBD',r'', document)


def to_sparse(vector: list[float]) -> list[tuple]:
    sparse_vector = []
    for index, value in enumerate(vector):
        if value != 0: 
            sparse_vector.append( (index, value) )
    
    return sparse_vector