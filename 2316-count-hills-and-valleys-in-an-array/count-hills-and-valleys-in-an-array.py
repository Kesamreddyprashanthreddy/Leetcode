class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                n.append(nums[i])
        
        for i in range(1,len(n)-1):
            if n[i] > n[i-1] and n[i] > n[i+1]:
                count += 1
                
            if n[i] < n[i-1] and n[i] < n[i+1]:
                count += 1

        return count