class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        '''
        dfs - flood fill
        case: [[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]]        
        follow up 1: only count island that are at the center of the ocean(not at the edge of the map)
        follow up 2: distinct islands(ref:https://leetcode.com/problems/number-of-distinct-islands/)
        '''
        visited = set()
        def dfs(i,j,d):
            if (i,j) in visited:
                return
            visited.add((i,j))
            grid[i][j] = 0
            current_path.append(d)
            if i+1 < m and grid[i+1][j] == 1:
                dfs(i+1,j,'d')
            if i-1 >= 0 and grid[i-1][j] == 1:
                dfs(i-1,j,'u')
            if j+1 < n and grid[i][j+1] == 1:
                dfs(i,j+1,'r')
            if j-1 >= 0 and grid[i][j-1] == 1:
                dfs(i,j-1,'l')
            current_path.append('x')
            return
        
        shapes = set()
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        c = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    current_path = []
                    dfs(i,j,'x')
                    shapes.add(tuple(current_path))
                   
        return len(shapes)
