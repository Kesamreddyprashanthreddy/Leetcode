class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(1,k+1):
            mini = min(nums)
            for j in range(len(nums)):
                if nums[j] == mini:
                    nums[j] = mini*multiplier
                    break
        return nums
                
                
