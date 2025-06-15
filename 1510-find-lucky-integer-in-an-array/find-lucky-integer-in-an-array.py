class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        result = []
        for n in d:
            if n == d[n]:
                result.append(n)
        return max(result) if result  else -1
