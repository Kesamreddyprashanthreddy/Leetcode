class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        sum_res = 0
        prod_res = 1
        while num > 0:
            last_digit = num % 10
            sum_res += last_digit
            prod_res *= last_digit
            num = num // 10
        total_res = sum_res + prod_res
        if n % total_res == 0:
            return True
        else:
            return False
