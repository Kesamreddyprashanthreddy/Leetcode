class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = []
        for num in arr:
            if num == arr.count(num):
                result.append(num)
        if result:
            return max(result)
        else:
            return -1