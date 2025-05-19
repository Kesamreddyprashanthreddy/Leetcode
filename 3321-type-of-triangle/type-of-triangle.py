class Solution:
    def triangleType(self, nums: List[int]) -> str:       
        nums.sort()
        a,b,c = nums
        if a + b <= c:
            return "none"
        if len(set(nums)) == 1:
            return "equilateral"
        elif len(set(nums)) == 2:
            return "isosceles"
        else:
            return "scalene"

             
