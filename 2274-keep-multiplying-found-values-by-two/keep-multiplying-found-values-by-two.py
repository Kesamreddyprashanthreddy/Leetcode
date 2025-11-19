class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        count = original
        while count in nums:
            count *= 2
        return count
        