class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top = float('inf')       
        bottom = float('-inf')    
        left = float('inf')
        right = float('-inf')

        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    top = min(top,i)
                    bottom = max(bottom,i)
                    left = min(left,j)
                    right = max(right,j)
        if top == float('inf'):
            return 0            
        Area = (bottom - top+1)*(right - left + 1)
        return Area