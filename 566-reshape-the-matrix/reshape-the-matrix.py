class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        

        if r * c != len(mat) * len(mat[0]):
            return mat
        else:
            m,n = len(mat),len(mat[0])
            flatten_arr = []
            for i in range(m):
                for j in range(n):
                    flatten_arr.append(mat[i][j])

            reshaped_arr = []
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(flatten_arr[i * c + j])
                reshaped_arr.append(row)
            return reshaped_arr 