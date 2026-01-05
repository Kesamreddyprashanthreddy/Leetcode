class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_abs = float("inf") 
        total = 0 
        count = 0 
        for row in matrix:
            for val in row:
                total += abs(val)
                min_abs = min(min_abs,abs(val))
                if val < 0:
                    count += 1
        if count % 2 == 1:
            total -= 2 * min_abs
        return total