class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x : x[1])
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        ans = 0
        for start, end in events:
            day = find(start)
            if day > end:
                continue
            parent[day] = find(day + 1) 
            ans += 1
        return ans

        
            