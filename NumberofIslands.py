class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        dfs - flood fill
        follow up 1: only count island that are at the center of the ocean(not at the edge of the map)
        follow up 2: distinct islands(ref:https://leetcode.com/problems/number-of-distinct-islands/)
        '''
        def dfs(i,j):
            grid[i][j] = '0'
            if i+1 < m and grid[i+1][j] == '1':
                dfs(i+1,j)
            if i-1 >= 0 and grid[i-1][j] == '1':
                dfs(i-1,j)
            if j+1 < n and grid[i][j+1] == '1':
                dfs(i,j+1)
            if j-1 >= 0 and grid[i][j-1] == '1':
                dfs(i,j-1)
            return
        
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        c = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    c += 1
        return c
