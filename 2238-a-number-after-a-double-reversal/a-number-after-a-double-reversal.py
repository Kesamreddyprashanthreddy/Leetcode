class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        nums = list(str(num))
        if len(nums) == 1:
            return True
        if nums[-1] == "0":
            return False
        else:
            return True