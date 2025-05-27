class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        arr = []
        arr1 =  []
        for i in range(1,n+1):
            if i % m != 0:
                arr.append(i)
            else:
                arr1.append(i)

        sum_arr = sum(arr)
        sum_arr1 = sum(arr1)
        return sum_arr-sum_arr1

        