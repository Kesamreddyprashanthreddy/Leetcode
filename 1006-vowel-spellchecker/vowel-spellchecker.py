class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def devowel(word: str) -> str:
            return "".join('*' if c in vowels else c for c in word.lower())
        wordset = set(wordlist)
        cap_map = {}
        vowel_map = {}
        for word in wordlist:
            lower = word.lower()
            if lower not in cap_map:
                cap_map[lower] = word
            mask = devowel(word)
            if mask not in vowel_map:
                vowel_map[mask] = word

        ans = []
        for q in queries:
            if q in wordset: 
                ans.append(q)
            elif q.lower() in cap_map:  
                ans.append(cap_map[q.lower()])
            elif devowel(q) in vowel_map:  
                ans.append(vowel_map[devowel(q)])
            else:  
                ans.append("")
        return ans