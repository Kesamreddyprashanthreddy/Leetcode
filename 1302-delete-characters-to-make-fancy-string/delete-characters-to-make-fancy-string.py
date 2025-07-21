class Solution:
    def makeFancyString(self, s: str) -> str:
        string = ""
        count = 1
        string += s[0]
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                string += s[i]
        return string

            