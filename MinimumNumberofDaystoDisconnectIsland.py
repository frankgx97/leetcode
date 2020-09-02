class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j,g):
            if not 0<=i<m or not 0<=j<n or g[i][j] == 0:
                return
            g[i][j] = 0
            dfs(i+1,j,g)
            dfs(i-1,j,g)
            dfs(i,j+1,g)
            dfs(i,j-1,g)
            return
        def number_of_islands(g):
            no = 0
            for i in range(m):
                for j in range(n):
                    if g[i][j] == 1:
                        no += 1
                        dfs(i,j,g)
            return no
        
        c = copy.deepcopy(grid)
        if number_of_islands(c) != 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                x = copy.deepcopy(grid)
                if x[i][j] == 1:
                    x[i][j] = 0
                    if number_of_islands(x) != 1:
                        return 1
        return 2
