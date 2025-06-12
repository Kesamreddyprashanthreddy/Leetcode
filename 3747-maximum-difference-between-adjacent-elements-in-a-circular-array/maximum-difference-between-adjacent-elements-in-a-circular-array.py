class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(1,len(nums)):
            res = max(res,abs(nums[i-1] - (nums[i])))

            
        res = max(res,abs(nums[-1] - nums[0]))
        return res
                 
