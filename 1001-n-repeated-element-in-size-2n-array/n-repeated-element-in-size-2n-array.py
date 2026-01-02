class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num in dict:
                return num
            else:
                dict[num] = 1
