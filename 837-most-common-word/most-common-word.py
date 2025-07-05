class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if banned is None:
            return paragraph
        
        paragraph = paragraph.lower()
        for ch in string.punctuation:
            paragraph = paragraph.replace(ch,' ')

        paragraph = paragraph.split()
        
        uniq_banned = {}
        for s in paragraph:
            if s in uniq_banned:
                uniq_banned[s] += 1
            else:
                uniq_banned[s] = 1
        not_banned_value = 0
        for k in uniq_banned:
            if k not in banned:
                not_banned_value = max(not_banned_value,uniq_banned[k])
        
        not_banned_word = ""
        for key,value in uniq_banned.items():
            if value == not_banned_value and key not in banned:
                not_banned_word += key
        return not_banned_word
       