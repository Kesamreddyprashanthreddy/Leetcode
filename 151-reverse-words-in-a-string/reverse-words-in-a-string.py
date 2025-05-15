class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split()
        res = w[::-1]
        return " ".join(res)