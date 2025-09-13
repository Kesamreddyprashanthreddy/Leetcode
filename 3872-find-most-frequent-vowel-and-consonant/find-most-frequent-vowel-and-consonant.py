class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {}
        consonants = {}
        v = "aeiou"
        for char in s:
            if char in v:
                if char in vowels:
                    vowels[char] += 1
                else:
                    vowels[char] = 1
            else:
                if char in consonants:
                    consonants[char] += 1
                else:
                    consonants[char] = 1
        max_vowel = max(vowels.values()) if vowels else 0
        max_consonant = max(consonants.values()) if consonants else 0
        return  max_vowel + max_consonant