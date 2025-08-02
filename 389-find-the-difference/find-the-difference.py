class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = {}

        for l in s:
            if l in res:
                res[l] += 1
            else:
                res[l] = 1
        for l in t:
            if l not in res or res[l] == 0:
                return l
            else:
                res[l] -= 1