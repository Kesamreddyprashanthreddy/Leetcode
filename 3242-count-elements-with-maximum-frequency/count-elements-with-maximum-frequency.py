class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        res = {}
        m = 0
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1 
            m = max(m,res[num])
        add = sum(v for v in res.values() if v == m)
        return add
        