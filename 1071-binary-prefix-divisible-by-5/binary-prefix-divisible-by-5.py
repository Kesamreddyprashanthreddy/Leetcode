class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        arr = []
        curr = 0

        for num in nums:
            curr = (curr * 2 + num) % 5
            arr.append(curr == 0)
        return arr