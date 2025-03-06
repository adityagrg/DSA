class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [None] * len(graph)
        for i in range(len(graph)):
            if colors[i] is None:
                q = deque()
                q.append(i)

                color = 'r'
                colors[i] = color
    		    
                while q:
                    current = q.popleft()
                    color = 'b' if colors[current] == 'r' else 'r'
    
                    for neighour in graph[current]:
                        if colors[neighour] is None:
                            q.append(neighour)
                            colors[neighour] = color
                        elif colors[neighour] != color:
                            return False
                del q

        return True
