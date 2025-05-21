class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        res = {}
        for i in range(len(s)):
            if s[i]  in res:
                res[s[i]] += 1 
            else:
                res[s[i]] = 1
        a = list(res.values())
        if len(set(a)) == 1:
            return True
        else:
            return False
         