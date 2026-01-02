class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
                return num
            else:
                dict[num] = 1
