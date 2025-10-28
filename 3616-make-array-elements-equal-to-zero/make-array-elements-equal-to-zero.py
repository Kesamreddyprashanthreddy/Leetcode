class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        def simulate(start, direction):
            arr = nums[:]  
            curr = start
            dir_step = 1 if direction == 1 else -1
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir_step
                else:
                    arr[curr] -= 1
                    dir_step *= -1
                    curr += dir_step

            return all(x == 0 for x in arr)

        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):   
                    ans += 1
                if simulate(i, -1): 
                    ans += 1
        return ans