class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
    
        res = ""
        if (numerator < 0) ^ (denominator < 0):
            res += "-"
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator // denominator)
        remainder = numerator % denominator
        if remainder == 0:
            return res  
        
        res += "."
        remainder_map = {}   
        while remainder != 0:
            if remainder in remainder_map:       
                idx = remainder_map[remainder]
                res = res[:idx] + "(" + res[idx:] + ")"
                break
            remainder_map[remainder] = len(res)
            remainder *= 10
            res += str(remainder // denominator)
            remainder %= denominator   
        return res