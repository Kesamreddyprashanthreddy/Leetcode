class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        mini = 0
        zeros = 0
        for i in range(len(nums2)):
            if nums2[i] == 0:
                nums2[i] = 1
                zeros += 1
        arr2 = sum(nums2)
        mini += arr2
        zeros1 = 0
        for i in range(len(nums1)):
            if nums1[i] == 0:
                nums1[i] = 1
                zeros1 += 1
        arr1 = sum(nums1)
        if arr1 == arr2:
            return arr1
        else:
            if arr1 > arr2 and zeros == 0:
                return -1
            if arr2  > arr1 and zeros1 == 0:
                return -1
            return max(arr1,arr2)
        


            
                
                
                        