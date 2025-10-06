class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dp = [False] * n
        dp[0] = True
        reach = 0
        for i in range(n):
            if dp[i]:
                reach = max(reach,i+nums[i])
            if  i+ 1 < n and i + 1 <= reach:
                dp[i+1] = True
        return dp[n-1]