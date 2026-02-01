class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        a = float('inf')
        b = float('inf')
        for num in nums[1:]:
            if num < a:
                b = a
                a = num
            elif num < b:
                b = num
        return first + a + b
