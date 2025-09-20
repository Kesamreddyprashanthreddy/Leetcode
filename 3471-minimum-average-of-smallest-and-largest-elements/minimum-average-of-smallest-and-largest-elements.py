class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        min_avg = []
        
        for i in range(len(nums)//2):
            max_element = max(nums)
            min_element = min(nums)
            avg = (max_element+min_element) / 2
            min_avg.append(avg)
            nums.remove(max_element)
            nums.remove(min_element)
        return min(min_avg)
