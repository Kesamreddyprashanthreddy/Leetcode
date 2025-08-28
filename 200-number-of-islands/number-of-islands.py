class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(i,j,visited,grid):
            m,n = len(grid),len(grid[0])
            d = [(-1,0),(1,0),(0,-1),(0,1)]
            q = deque()
            q.append((i,j))
            visited[i][j] = True

            while q:
                x,y = q.popleft()
                for dx,dy in d:
                    nx,ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == "1" and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx,ny))


        m,n = len(grid),len(grid[0])
        count = 0
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i,j,visited,grid)
                    count += 1
        return count



