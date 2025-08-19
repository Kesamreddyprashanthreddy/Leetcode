class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        num  = max(nums)
        idx = nums.index(num)
        nums.remove(num)
        for i in range(len(nums)):
            if num < 2 * nums[i]:
                return -1
        return idx