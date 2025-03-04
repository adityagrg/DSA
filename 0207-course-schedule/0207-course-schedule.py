class Solution:
    def util(self, adj, elementToBeChecked, q):
        visited = set()
        visited.add(elementToBeChecked)
        while q:
            current = q.popleft()
            print("current = " + str(current))
            if current in adj:
                for element in adj[current]:
                    if element == elementToBeChecked:
                        return False
                    
                    visited.add(element)
                    
                    if element not in visited:
                        q.append(element)
        
        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [None] * numCourses
        for prerequisite in prerequisites:
            if adj[prerequisite[1]] is not None:
                adj[prerequisite[1]].append(prerequisite[0])
            else:
                adj[prerequisite[1]] = [prerequisite[0]]
        
        in_degree = [0] * numCourses
        
        for i in range(numCourses):
            if adj[i] is not None:
                for j in adj[i]:
                    in_degree[j] += 1
        
        q = deque()
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        ans = []
        while q:
            current = q.popleft()
            ans.append(current)
            if adj[current] is not None:
                for neighour in adj[current]:
                    in_degree[neighour] -= 1
                    if in_degree[neighour] == 0:
                        q.append(neighour)
        
        if len(ans) == numCourses:
            return True
        else:
            return False