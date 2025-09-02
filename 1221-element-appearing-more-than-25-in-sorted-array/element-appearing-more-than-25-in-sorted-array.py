class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        res = max(count.values())
        for n in count:
            if count[n] == res:
                return n

        