class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        count = 0
        if letter not in s:
            return count
        for ch in s:
            if ch == letter:
                count += 1
        return math.floor(count / n *100)