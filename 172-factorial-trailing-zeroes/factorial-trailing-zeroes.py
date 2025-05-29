class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        count = 0
        sys.set_int_max_str_digits(100000)

        res = 1
        for i in range(1,n+1):
            res *= i
        a = str(res)[::-1]
        for num in a:
            if num == '0':
                count += 1
            else:
                break
        return count
        
        