class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = sum(nums)
        operations = 0
        while result % k != 0:
            result = result - 1
            operations += 1
        return operations