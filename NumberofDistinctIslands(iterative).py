class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        '''
        dfs iterative - flood fill
        case: [[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]]        
        follow up 1: only count island that are at the center of the ocean(not at the edge of the map)
        follow up 2: distinct islands(ref:https://leetcode.com/problems/number-of-distinct-islands/)
        '''
      
        def dfs_iterative(i,j):
            path = []
            queue = [(i,j,'')]
            while queue:
                curr = queue.pop(-1)
                i = curr[0]
                j = curr[1]
                
                path += [curr[2]]
                grid[i][j] = 0
                if i+1 < m and grid[i+1][j] == 1 and (i+1,j) not in visited:
                    queue += [(i+1,j,'d')]
                    visited.add((i+1,j))
                else:
                    path.append('x')
                if i-1 >= 0 and grid[i-1][j] == 1 and (i-1,j) not in visited:
                    queue += [(i-1,j,'u')]
                    visited.add((i-1,j))
                else:
                    path.append('x')
                if j+1 < n and grid[i][j+1] == 1 and (i,j+1) not in visited:
                    queue += [(i,j+1,'r')]
                    visited.add((i,j+1))
                else:
                    path.append('x')
                if j-1 >= 0 and grid[i][j-1] == 1 and (i,j-1) not in visited:
                    queue += [(i,j-1,'l')]
                    visited.add((i,j-1))
                else:
                    path.append('x')
                
            return path


        visited = set()
        shapes = set()
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        c = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = dfs_iterative(i,j)
                    shapes.add(tuple(curr))
        return len(shapes)
