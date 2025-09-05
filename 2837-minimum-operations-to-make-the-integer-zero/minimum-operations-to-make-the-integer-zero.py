class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(1,60):
            res = num1 - i * num2
            if res < 0:
                return -1
            if res >= i and bin(res).count('1') <= i:
                return i
        return -1

            