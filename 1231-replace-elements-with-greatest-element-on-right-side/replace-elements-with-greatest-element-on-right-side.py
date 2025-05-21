class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        max_val= -1
        for i in reversed(range(len(arr))):
           res.append(max_val)
           max_val = max(max_val,arr[i])
        res.reverse()     
        return res
