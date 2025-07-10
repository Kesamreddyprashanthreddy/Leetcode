class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        m,n = len(image),len(image[0])
        original = image[sr][sc]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        q = deque()
        q.append((sr,sc))
        image[sr][sc] = color
        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                nx,ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == original :
                    image[nx][ny] = color
                    q.append((nx,ny))
        return image
