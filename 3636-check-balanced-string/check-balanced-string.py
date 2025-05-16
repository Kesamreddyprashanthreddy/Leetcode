class Solution:
    def isBalanced(self, num: str) -> bool:
        # arr = list(num)
        odd_sum = 0
        even_sum = 0
        for i in range(len(num)):
            if int(i) % 2 != 0:
                odd_sum += int(num[i])
            if int(i) % 2 == 0:
                even_sum += int(num[i])
        if odd_sum == even_sum:
            return True
        else:
            return False