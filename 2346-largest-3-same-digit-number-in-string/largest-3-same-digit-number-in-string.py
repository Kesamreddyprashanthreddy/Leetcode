class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ''
        for i in range(len(num)-2):
            substring = num[i:i+3]
            if substring[0] == substring[1] == substring[2]:
                if substring > largest:
                    largest = substring
        return largest
            