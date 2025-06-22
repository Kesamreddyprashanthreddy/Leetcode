class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        st = ''
        res = []
        for i in range(len(s)):
            if len(st) < k:
                st += s[i]
            if len(st) == k:
                res.append(st)
                st = ''
        
        if st:
            st += fill * (k - len(st))
            res.append(st)
        return res