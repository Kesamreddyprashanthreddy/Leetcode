class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        for word in words:
            if stack and sorted(stack[-1]) == sorted(word):
                continue  
            stack.append(word)

        return stack