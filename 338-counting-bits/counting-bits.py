class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        arr = []
        for i in range(n+1):
            count = 0
            num = i
            while num > 0:
                if num & 1:
                    count += 1
                num = num >> 1
            arr.append(count)
        return arr
        