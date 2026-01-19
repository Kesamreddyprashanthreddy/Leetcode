class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        g = {}
        for a,b in edges:
            if a not in g:
                g[a] = []
            if b not in g:
                g[b] = []
            g[a].append(b)
            g[b].append(a)
        
        center = -1
        count = 0
        for node in g:
            c = len(g[node])
            if c > count:
                count = c
                center = node
        return center
