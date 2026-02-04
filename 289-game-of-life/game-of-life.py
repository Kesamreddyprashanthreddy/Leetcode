class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for dx,dy in d:
                    nx,ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if abs(board[nx][ny]) == 1:
                            count += 1
                            
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = -1
                else:
                    if count == 3:
                        board[i][j] = 2
                
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0