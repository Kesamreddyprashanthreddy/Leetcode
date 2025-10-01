class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        con = 0
        while left < right:
            s=""
            s += str(nums[left])
            s += str(nums[right])
            con += int(s)
            
            left += 1
            right -= 1
        if len(nums) % 2 != 0:
            mid = (0 + len(nums)-1) // 2
            con += nums[mid]
        return con 
