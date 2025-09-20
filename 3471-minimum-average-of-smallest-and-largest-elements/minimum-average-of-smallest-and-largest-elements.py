class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        min_avg = float("inf")
        n = len(nums)
        for i in range(n // 2):
            avg =( nums[i] + nums[n-1-i]) / 2
            min_avg = min(avg,min_avg)
        return min_avg