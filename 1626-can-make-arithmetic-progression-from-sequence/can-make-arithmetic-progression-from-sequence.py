class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        r = set()
        for i in range(1,len(arr)):
            r.add(arr[i-1] - arr[i])
        return True if len(r) == 1 else False
