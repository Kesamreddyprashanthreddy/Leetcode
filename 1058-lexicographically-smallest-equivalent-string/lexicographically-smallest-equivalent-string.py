class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        from collections import defaultdict, deque

        adj = defaultdict(list)
        for a, b in zip(s1, s2):
            adj[a].append(b)
            adj[b].append(a)

        mini = {}
        visited = set()

        def bfs(start):
            queue = deque([start])
            component = set([start])
            visited.add(start)

            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        component.add(nei)
                        queue.append(nei)

            smallest = min(component)
            for ch in component:
                mini[ch] = smallest

        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch not in visited:
                bfs(ch)

        return ''.join(mini.get(ch, ch) for ch in baseStr)