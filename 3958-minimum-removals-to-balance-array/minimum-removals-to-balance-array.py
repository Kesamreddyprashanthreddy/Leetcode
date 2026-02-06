class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        count = 0
        for right in range(len(nums)):
            while nums[right] > nums[left] * k:
                left += 1
            
            count = max(count,right-left + 1)
        return len(nums) - count