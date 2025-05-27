class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:   
        arr = 0
        arr1 = 0 
        for i in range(1,n+1):
            if i % m != 0:
                arr += i
            else:
                arr1 += i
        return arr-arr1

        