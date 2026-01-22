class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n  = len(grid),len(grid[0])
        dist = [[float('inf')] *n for _ in range(m)]
        dist[0][0] = 0
        q = deque()
        q.append([0,0])
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x,y = q.popleft()
            for dx,dy in d:
                nx,ny = x + dx, y + dy
                if 0 <= nx < m and  0 <= ny < n:
                    cost = grid[nx][ny]
                    newdist = dist[x][y] + cost
                    if newdist < dist[nx][ny]:
                        dist[nx][ny] = newdist
                    
                        if cost == 0:
                            q.appendleft((nx,ny))
                        else:
                            q.append((nx,ny))
        return dist[m-1][n-1]
