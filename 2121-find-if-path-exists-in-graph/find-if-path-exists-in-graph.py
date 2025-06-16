class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        q  = deque()
        visited[source] = True
        q.append(source)
        while q:
            curr = q.popleft()
            if curr == destination:
                return True
           
            for x in graph[curr]:
                if not visited[x]:
                    visited[x] = True
                    q.append(x)
        return False


