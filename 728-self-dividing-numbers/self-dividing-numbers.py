class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left,right+1):
            a = i
            valid = True
            while a > 0:
                d =  a % 10
                if d == 0 or i % d != 0 :
                    valid = False
                    break
                if i % d == 0:
                    a = a // 10
            if valid:       
                res.append(i)
        return res
                    
