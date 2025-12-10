class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                x = nums[i]
                y = nums[j]
                if abs(x-y) <= min(x,y):
                    res = max(res,x^y)
        return res