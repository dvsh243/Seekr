import re


def cleanData(words: list) -> list:

    for i in range(len(words)):
        words[i] = re.sub(r'[,\'./()]|\sBD',r'', words[i])
    return words



# class Matrix:

#     def __init__(self, matrix: list[list]):
#         self.matrix = matrix

    
#     def to_csr(self):
#         pass
    
#     def to_dense(self):
#         pass
        
