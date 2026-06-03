class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        n = len(nums)
        for i in  range(n):
            dict = {}
            sub_array = nums[i: i+k-1+1]
            for num in sub_array:
                dict[num] = dict.get(num,0)+1
            
            result = sorted(dict.items(),key = lambda x : (-x[1],-x[0]))
            x_num = result[:x]
            total = 0
            for val in x_num:
                total += val[0]*val[1]
            res.append(total)
        return res[0:n-k+1]
            