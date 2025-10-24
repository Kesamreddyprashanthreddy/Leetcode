class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x):
            from collections import Counter
            s = str(x)
            cnt = Counter(s)
            for ch, c in cnt.items():
                if c != int(ch):
                    return False
            return True
        
        x = n + 1
        while True:
            if is_balanced(x):
                return x
            x += 1