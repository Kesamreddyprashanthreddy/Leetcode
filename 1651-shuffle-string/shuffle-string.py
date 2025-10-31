class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:      
        res = [""]*len(s)
        for idx,ch in enumerate(s):
            res[indices[idx]] = ch
        return "".join(res)

