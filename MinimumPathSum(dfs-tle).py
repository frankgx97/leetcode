import math
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(i,j,mi):
            if i == len(grid)-1 and j == len(grid[0])-1:
                return mi+grid[i][j]
            if i+1<len(grid):
                down = dfs(i+1,j,mi+ grid[i][j])
            else:
                down = math.inf
            if j+1<len(grid[0]):
                right = dfs(i,j+1,mi+ grid[i][j])
            else:
                right = math.inf
            return min(right,down)
        return dfs(0,0,0)
