class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ele = max(arr)
        count = 0
        for num in arr:
            if ele == num:
                return count
            count += 1
        
