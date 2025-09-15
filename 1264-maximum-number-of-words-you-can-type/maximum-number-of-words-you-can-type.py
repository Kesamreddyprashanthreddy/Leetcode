class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broken = set(brokenLetters)
        count = 0
        for char in words:
            if not any(ch in broken for ch in char):
                count += 1
        return count
        