class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        def word_types(s):
            if s in memo:
                return memo[s]
            if s == "":
                return [""]
            words = []
            for word in wordDict:
                if s.find(word) == 0:
                    suffix = s[len(word):]
                    res = word_types(suffix)
                    for ch in res:
                        if ch:
                            words.append(word + " " + ch)
                        else:
                            words.append(word)
                       
            memo[s] = words
            return words
        
        return word_types(s)

            