class Solution:
    def generate(self, numRows: int,memo={}) -> List[List[int]]:
        memo = {}
        def pascal(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            
            if col == 0 or col == row:
                return 1
            memo[(row, col)] = pascal(row-1, col-1) + pascal(row-1, col)
            return memo[(row, col)]
        
        triangle = []
        for r in range(numRows):
            row_vals = []
            for c in range(r+1):
                row_vals.append(pascal(r, c))
            triangle.append(row_vals)
        
        return triangle
        
                
