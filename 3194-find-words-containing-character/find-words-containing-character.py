class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            if words[i].count(x):
                result.append(i)
        return result