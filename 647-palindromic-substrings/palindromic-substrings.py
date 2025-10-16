class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                c = s[i:j+1]
                if c == c[::-1]:
                    count += 1
        return count
