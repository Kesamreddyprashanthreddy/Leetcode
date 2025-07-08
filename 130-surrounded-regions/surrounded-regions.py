class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m,n = len(board),len(board[0])

        q = deque()
        for i in range(m):
            if board[i][0] == 'O':
                q.append((i,0))
            if board[i][n-1] == 'O':
                q.append((i,n-1))
        
        for i in range(n):
            if board[0][i] == "O":
                q.append((0,i))
            if board[m-1][i] == "O":
                q.append((m-1,i))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            x,y = q.popleft()
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                board[x][y] = "#"
                for dx,dy in directions:
                    q.append((x + dx,y + dy))
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                
                if board[i][j] == "#":
                    board[i][j] = "O"
        return board