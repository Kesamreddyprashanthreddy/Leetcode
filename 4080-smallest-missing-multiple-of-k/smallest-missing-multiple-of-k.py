class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = k
        nums = set(nums)
        while True:
            if i % k == 0:
                if i not in nums:
                    return i
            
            i += k
        