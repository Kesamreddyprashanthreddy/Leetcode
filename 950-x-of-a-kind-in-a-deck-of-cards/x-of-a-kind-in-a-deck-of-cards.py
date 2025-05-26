class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        count = {}
        for card in deck:
            count[card] = count.get(card, 0) + 1

        values = list(count.values())
        def find_gcd(arr):
            return reduce(gcd, arr)

        return find_gcd(values) >= 2