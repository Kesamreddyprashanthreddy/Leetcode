class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = min(abs(arr[i] - arr[i-1]) for i in range(1,len(arr)))
        res = []
        for i in range(1,len(arr)):
            if min_diff == abs(arr[i] - arr[i-1]):
                res.append([arr[i-1],arr[i]])
        return res
        