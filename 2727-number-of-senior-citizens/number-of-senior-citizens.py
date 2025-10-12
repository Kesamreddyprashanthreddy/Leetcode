class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for ch in  details:
            s = int(ch[11:13])
            if s > 60:
                count += 1
        return count
