class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def dfs(queue,grid):
            lenx = len(grid)
            leny = len(grid[0])
            q = queue
            counter = len(q)
            days = 0
            while len(q) > 0:
                currx = q[0][0]
                curry = q[0][1]
                q.pop(0)
                counter -= 1
                
                if currx+1 >= 0 and currx+1 < lenx and grid[currx+1][curry] == 1:
                    grid[currx+1][curry] = 2
                    q.append([currx+1,curry])
                if curry+1 >= 0 and curry+1 < leny and grid[currx][curry+1] == 1:
                    grid[currx][curry+1] = 2
                    q.append([currx,curry+1])
                if currx-1 >= 0 and currx-1 < lenx and grid[currx-1][curry] == 1:
                    grid[currx-1][curry] = 2
                    q.append([currx-1,curry])
                if curry-1 >= 0 and curry-1 < leny and grid[currx][curry-1] == 1:
                    grid[currx][curry-1] = 2
                    q.append([currx,curry-1])

                if len(q) > 0 and counter <= 0:
                    days += 1
                    counter = len(q)
                    
            for i in grid:
                for j in i:
                    if j == 1:
                        return -1
            
            return days
        
        initial = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    initial.append([i,j])
        return dfs(initial,grid)
                
            
            
            
