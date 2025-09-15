class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = {}
        t1 = {}
        for i in range(len(s)):
            if s[i] in s1:
                s1[s[i]] += 1        
            else:
                s1[s[i]] = 1
            
            if t[i] in t1:
                t1[t[i]] += 1
            else:
                t1[t[i]] = 1
        
        
        return s1 == t1
        
        