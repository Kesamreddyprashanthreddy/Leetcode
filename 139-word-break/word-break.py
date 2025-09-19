class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def words(s):
            if s in memo:
                return memo[s]
            if s == "":
                return True
            
            for word in wordDict:
                if s.find(word) == 0:
                    suffix = s[len(word):]
                    if words(suffix) == True:
                        memo[s] = True
                        return True
            memo[s] =False
            return False
        return words(s)