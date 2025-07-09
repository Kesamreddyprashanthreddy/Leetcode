class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n = len(grid1),len(grid1[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def bfs(x,y):
            queue = deque()
            queue.append((x,y))
            is_sub_island = True
            grid2[x][y] = 0
            while queue:
                i,j = queue.popleft()
                if grid1[i][j] == 0:
                    is_sub_island = False
                
                for dx,dy in directions:
                    ni,nj = i+dx,j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid2[ni][nj] == 1:
                        grid2[ni][nj] = 0
                        queue.append((ni,nj))
            return is_sub_island
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if bfs(i,j):
                        count += 1
        return count

            


        
        
        