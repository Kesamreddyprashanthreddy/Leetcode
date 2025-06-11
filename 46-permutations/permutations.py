class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])  # Append a copy of path
                return

            for num in nums:
                if num not in used:
                    used.add(num)
                    path.append(num)
                    backtrack(path, used)
                    path.pop()
                    used.remove(num)

        backtrack([], set())
        return result
