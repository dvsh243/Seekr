
class Matrix:

    def __init__(self, matrix: list[list]) -> None:
        self.matrix = matrix
        self.max_col = self.get_max_column()
        self.dense_matrix = [None for _ in range(len(matrix))]
        self.to_dense()
        print("dense matrix created.")
    
    def __repr__(self) -> str:
        return f"<Matrix: {len(self.matrix)}>"
    

    def get_max_column(self) -> int:
        max_col = -1

        for row in self.matrix:
            for c, value in row:
                max_col = max(max_col, c)
        
        return max_col
    

    def to_dense(self) -> None:

        for i, row in enumerate(self.matrix):
            new_row = [0 for _ in range(self.max_col + 1)]
            for c, value in row:
                new_row[c] = value
            self.dense_matrix[i] = new_row

    
    def target_dense(self, target_list) -> list:
        res = [0 for _ in range(self.max_col + 1)]

        for idx, value in target_list:
            if idx > self.max_col: continue
            res[idx] = value
        
        return res

    def clear_memory(self) -> None:
        del self.matrix
        del self.dense_matrix
        print("deleted `self.matrix` and `self.dense_matrix`")
