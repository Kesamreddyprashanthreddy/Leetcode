class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            res = bin(i).count('1')
            arr.append(res)
        return arr