class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_value = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                max_value = max((nums[i]-1)*(nums[j]-1),max_value)
        return max_value