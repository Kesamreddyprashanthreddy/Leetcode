class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        max_freq = max(dict.values())
        count = 0
        for num in dict:
            if dict[num] == max_freq:
                count += max_freq
        return count