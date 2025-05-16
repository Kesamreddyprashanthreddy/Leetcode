class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[1,i] for i in range(n)]
        def dist(s1, s2):
            d = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    d += 1
            return d      
        for i in range(1, n):
            max_len, max_i = -1, -1
            for j in range(i):
                if groups[i] == groups[j] or len(words[i]) != len(words[j]) or dist(words[i], words[j]) != 1:
                    continue
                if dp[j][0] > max_len:
                    max_len = dp[j][0]
                    max_i = j
            if max_len != -1:
                dp[i][0] = max_len + 1
                dp[i][1] = max_i
        max_d = [-1,-1]
        max_i = -1
        for i, d in enumerate(dp):
            if d[0] > max_d[0]:
                max_d = d
                max_i = i
        ans = [words[max_i]]
        i = max_i
        while i != max_d[1]:
            i = max_d[1]
            max_d = dp[i]
            ans.append(words[i])
        return ans[::-1]