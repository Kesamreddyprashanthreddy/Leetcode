class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        arr = "".join(map(str,digits))
        even_arr = []
        for num in permutations(arr,3):
            if num[0] != '0':
                res = int("".join(num))
                if res % 2 == 0:
                    even_arr.append(res)
        even_arr.sort()
        result = list(set(even_arr))
        result.sort()
        return result     