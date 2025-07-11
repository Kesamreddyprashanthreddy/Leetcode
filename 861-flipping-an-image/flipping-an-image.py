class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        m,n = len(image),len(image[0])

        reverse_row = []
        for rows in image:
            rows.reverse()
            reverse_row.append(rows)
    

        for i in range(m):
            for j in range(n):
                if reverse_row[i][j] == 1:
                    reverse_row[i][j] = 0
                else:
                    reverse_row[i][j] = 1
        return reverse_row
