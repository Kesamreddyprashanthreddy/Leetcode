class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        twice = {}
        res = []
        for num in nums:
            if num in twice:
                twice[num] += 1
                res.append(num)
            else:
                twice[num] = 1
        return res
        