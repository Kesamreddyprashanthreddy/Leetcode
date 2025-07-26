class Solution:
    
    def getPermutations(self,nums,idx,ans):
        if idx == len(nums):
            ans.append(nums[:])
            return
        for i in range(idx,len(nums)):
            nums[idx],nums[i] = nums[i],nums[idx]
            self.getPermutations(nums,idx+1,ans)
            nums[idx],nums[i] = nums[i], nums[idx]


    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.getPermutations(nums,0,ans)
        return ans
        