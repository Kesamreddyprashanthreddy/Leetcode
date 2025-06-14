class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_val = float('-inf')
        min_val = float("inf")

        for d1 in '0123456789':
            for d2 in '0123456789':
                if d1 == d2:
                    continue
                new_s = s.replace(d1,d2)
                new_num = int(new_s)
                max_val = max(max_val,new_num)
                min_val = min(min_val,new_num)
        return max_val-min_val
                