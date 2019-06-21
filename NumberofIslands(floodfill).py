class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def fill(i,j):
            grid[i][j] = '0'
            if i < len(grid)-1 and grid[i+1][j] == '1':
                fill(i+1,j)
            if i > 0 and grid[i-1][j] == '1':
                fill(i-1,j)
            if j < len(grid[0])-1 and grid[i][j+1] == '1':
                fill(i,j+1)
            if j > 0 and grid[i][j-1] == '1':
                fill(i,j-1)
            return
        
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    fill(i,j)
                    c += 1
        return c
