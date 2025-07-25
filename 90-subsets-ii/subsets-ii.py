class Solution:

    def getAllSubsets(self,nums,ans,i,arraySubset):
        if (i == len(nums)):
            arraySubset.append(ans[:])
            return
        ans.append(nums[i])
        self.getAllSubsets(nums,ans,i+1,arraySubset)

        ans.pop()
        idx = i+1
        while idx < len(nums) and nums[idx] == nums[idx-1]:
            idx += 1
        
        self.getAllSubsets(nums,ans,idx,arraySubset)
        

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arraySubset = []
        ans = []
        self.getAllSubsets(nums,ans,0,arraySubset)
        return arraySubset
        