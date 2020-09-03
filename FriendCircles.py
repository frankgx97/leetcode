class Solution:
    '''
    bfs/dfs - number of islands
    '''
    def findCircleNum(self, M: List[List[int]]) -> int:
        def construct(M):
            graph = {}
            for i in range(len(M)):
                for j in range(len(M)):
                    if M[i][j] == 1:
                        if i not in graph:
                            graph[i] = [j]
                        else:
                            graph[i].append(j)
            return graph
                    
        def bfs(start):
            if start in visited:
                return False
            queue = [start]
            while queue:
                curr = queue.pop(0)
                visited.add(curr)
                for i in graph[curr]:
                    if i not in visited:
                        queue.append(i)
            return True
        
        ans = 0
        graph = construct(M)
        visited = set()
        for i in range(len(M)):
            if bfs(i):
                ans += 1
        return ans
