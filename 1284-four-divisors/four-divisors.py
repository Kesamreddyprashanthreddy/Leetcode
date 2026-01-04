class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:    
        ans = []
        for num in nums:
            d = []
            for i in range(1,int(num**0.5)+1):
                if num % i == 0:
                    d.append(i)
                    if i != num // i:
                        d.append(num // i)
                if len(d) > 4:
                    break
            
            if len(d) == 4:
                s = sum(d)
                ans.append(s)
            else:
                d = []
        return sum(ans) if ans else 0