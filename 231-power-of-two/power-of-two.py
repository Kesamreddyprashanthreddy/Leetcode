class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 1:
            return True
        if n < 1 or n % 2 != 0:
            return False
        else:
            return self.isPowerOfTwo(n/2)

        