class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        freq = [0] * (n + 1)

        for l, r in queries:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1
        for i in range(1, n):
            freq[i] += freq[i - 1]
        for i in range(n):
            if nums[i] > freq[i]:
                return False

        return True