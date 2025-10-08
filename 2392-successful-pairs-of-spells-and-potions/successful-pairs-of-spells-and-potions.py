class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        n = len(potions)
        for spell in spells:
            min_needed = (success + spell - 1) // spell  
            idx = bisect.bisect_left(potions, min_needed)
            pairs.append(n - idx)  
        return pairs

