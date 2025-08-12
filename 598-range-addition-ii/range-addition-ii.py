class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        min_a = []
        min_b = []
        for a,b in ops:
            min_a.append(a)
            min_b.append(b)
        return min(min_a)*min(min_b)


