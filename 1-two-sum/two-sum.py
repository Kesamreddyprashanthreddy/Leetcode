class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in ans:
                return [ans[res],i]
            ans[num] = i
        


