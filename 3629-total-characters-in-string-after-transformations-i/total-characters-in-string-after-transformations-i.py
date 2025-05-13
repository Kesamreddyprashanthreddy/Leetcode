class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        from collections import Counter
        MOD = 10**9 + 7
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):
                if i == 25:  # 'z'
                    new_freq[0] = (new_freq[0] + freq[25]) % MOD  # 'a'
                    new_freq[1] = (new_freq[1] + freq[25]) % MOD  # 'b'
                else:
                    new_freq[i + 1] = (new_freq[i + 1] + freq[i]) % MOD
            freq = new_freq

        return sum(freq) % MOD