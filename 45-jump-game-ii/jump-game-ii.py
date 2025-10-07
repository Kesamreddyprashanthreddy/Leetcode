class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        count = 0
        end = 0
        reach = 0
        for i in range(n-1):
            reach = max(reach,i + nums[i])
            if i == end:
                count += 1
                end = reach
        return count