class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        def find(d):
            for i in range(m):
                for j in range(n):
                    if A[i][j] == d:
                        return(i,j)
            return (-1,-1)
        
        def dfs(x,y):
            if x >= m or x < 0 or y >= n or y < 0 or A[x][y] != 1:
                return
            A[x][y] = 2
            land.append((x,y,2))
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            return
        
        def bfs(x,y):
            queue = land
            while queue:
                inner = queue[:]
                queue = []
                visited = set()
                for i in inner:
                    x,y,st = i
                    if x >= m or x < 0 or y >= n or y < 0 or (x,y) in visited:
                        continue
                    visited.add((x,y))
                    if A[x][y] == 1:
                        return st
                    if A[i[0]][i[1]] == 0:
                        A[i[0]][i[1]] = st
                    queue.append((i[0]+1,i[1],st+1))
                    queue.append((i[0]-1,i[1],st+1))
                    queue.append((i[0],i[1]+1,st+1))
                    queue.append((i[0],i[1]-1,st+1))
            
        m = len(A)
        n = len(A[0])
        x,y = find(1)
        land = []
        dfs(x,y)
        r = bfs(x,y) - 3
        return r
