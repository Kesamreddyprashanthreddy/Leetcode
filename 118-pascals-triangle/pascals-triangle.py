class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = [[1]]
        for i in range(numRows-1):
            temp = [0] + r[-1] + [0]
            row = []
            for j in range(len(r[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            r.append(row)
        return r
                
