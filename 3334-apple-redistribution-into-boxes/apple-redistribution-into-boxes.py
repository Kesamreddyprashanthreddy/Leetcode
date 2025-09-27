class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total_apples = sum(apple)
        count = 0
        total = 0
        for num in capacity:
            if total_apples > total:
                total += num
                count += 1
            else:
                break
        return count