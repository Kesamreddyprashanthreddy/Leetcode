class Solution:

    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        return self.binary_search(nums,target,start,end)
    def binary_search(self,nums,target,start,end):
        if (start <= end):
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binary_search(nums,target,mid + 1,end)
            else:
                return self.binary_search(nums,target,start,mid-1)
        return -1
        