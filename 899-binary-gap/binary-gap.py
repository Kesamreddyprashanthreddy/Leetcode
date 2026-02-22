class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        gap = 0 
        idx = -1
        for i in range(len(b)):
            if b[i] == "1":
                if idx != -1:
                    gap = max(gap,i - idx)
                idx = i
        return gap