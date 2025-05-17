class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_arr = []
        odd_arr = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_arr.append(nums[i])
            else:
                odd_arr.append(nums[i])
        
        even_arr.extend(odd_arr)  
        return even_arr