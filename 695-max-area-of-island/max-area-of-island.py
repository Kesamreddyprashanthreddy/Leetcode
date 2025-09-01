class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        def bfs(i,j,grid):
            d = [(-1,0),(1,0),(0,-1),(0,1)]
            q = deque()
            q.append((i,j))
            visited[i][j] = True
            r = 0
            while q:
                x,y = q.popleft()
                r += 1
                for dx,dy in d:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny))

            return r

        visited = [[False] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    r = bfs(i,j,grid)
                    count = max(count,r)
        return count
                    

