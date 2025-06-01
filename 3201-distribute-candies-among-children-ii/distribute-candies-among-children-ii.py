class Solution:
    def count_ways(self, n, limit):
        total = 0
        for k in range(4): 
            val = n - k * (limit + 1)
            if val < 0:
                continue
            sign = (-1) ** k
            ways = comb(3, k) * comb(val + 2, 2)
            total += sign * ways
        return total

    def distributeCandies(self, n: int, limit: int) -> int:
        return self.count_ways(n, limit)