class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        s = str(num)
        for i in range(len(s)-k+1):
            sub = s[i:i+k]
            n = int(sub)
            if n  != 0 and num % n == 0:
                count += 1
        return count
