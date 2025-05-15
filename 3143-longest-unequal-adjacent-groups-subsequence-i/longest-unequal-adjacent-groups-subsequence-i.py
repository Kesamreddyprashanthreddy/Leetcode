class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not  words:
            return []
        r = [words[0]]
        prev = groups[0]
        for i in range(1,len(groups)):
            if groups[i] != prev:
                r.append(words[i])
                prev = groups[i]
        return r