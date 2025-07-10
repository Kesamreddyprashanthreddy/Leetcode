class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def bfs(x,y):
            perimeter = 0
            q = deque()
            q.append((x,y))
            visited = set()
            visited.add((x,y))
            while q:
                i,j = q.popleft()

                for dx,dy in directions:
                    ni,nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        if (ni,nj) not in visited:  
                            visited.add((ni,nj))           
                            q.append((ni,nj))
                    else:
                        perimeter += 1
            return perimeter
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return bfs(i,j)
        
        
