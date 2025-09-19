class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dict = {}
        for i,num in enumerate(sorted_nums):
            if num not in dict:
                dict[num] = i
        return [dict[num] for num in nums]
