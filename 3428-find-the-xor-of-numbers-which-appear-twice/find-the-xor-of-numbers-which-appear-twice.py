class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        a = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    a.append(nums[i])
        res = 0
        for i in range(len(a)):
            res ^= a[i]                
        if len(a) == 1:
            return a[0]
        elif len(a)>1:
            return res
        else:
            return 0
