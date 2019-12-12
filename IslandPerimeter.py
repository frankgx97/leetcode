class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        dfs - ac
        caution: reaching out of bound counts in perimeter
        '''
        '''
        def dfs(x,y):
            nonlocal perimeter
            if grid[x][y] != 1:
                return
            grid[x][y] = 2
            if 0<=x+1<m and grid[x+1][y] == 1:
                dfs(x+1,y)
            elif x+1 < 0 or x+1 >= m or grid[x+1][y] == 0:
                perimeter += 1
            if 0<=x-1<m and grid[x-1][y] == 1:
                dfs(x-1,y)
            elif x-1 < 0 or x-1 >= m or grid[x-1][y] == 0:
                perimeter +=1
            if 0<=y+1<n and grid[x][y+1] == 1:
                dfs(x,y+1)
            elif y+1 < 0 or y+1 >= n or grid[x][y+1] == 0:
                perimeter += 1
            if 0<=y-1<n and grid[x][y-1] == 1:
                dfs(x,y-1)
            elif y-1 < 0 or y-1 >= n or grid[x][y-1] == 0:
                perimeter +=1
            return
        '''
        def dfs(x,y):
            nonlocal perimeter
            if x<0 or x >=m or y<0 or y>=n or grid[x][y] == 0:
                perimeter += 1
                return
            if grid[x][y] != 1:
                return
            grid[x][y] = 2
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            return
            
            
                
        perimeter = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
        return perimeter
