class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        person1 = abs(z-x)
        person2 = abs(z-y)

        if person1 < person2:
            return 1
        elif person1 > person2:
            return 2
        else:
            return 0