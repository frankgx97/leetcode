class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = grid[i-1][j]+grid[i][j] if grid[i-1][j] < grid[i][j-1] else grid[i][j-1]+grid[i][j]
        return grid[m-1][n-1]
