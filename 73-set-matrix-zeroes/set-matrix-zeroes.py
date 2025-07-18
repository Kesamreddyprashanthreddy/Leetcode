class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        m,n = len(matrix),len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        
        for i in columns:
            for j in range(m):
                matrix[j][i] = 0
        return matrix
        
        