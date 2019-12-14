class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        follow up 1: only count island that are at the center of the ocean(not at the edge of the map)
        follow up 2: distinct islands(ref:https://leetcode.com/problems/number-of-distinct-islands/)
        '''
        '''
        bfs - ac
        '''
        def bfs(x,y):
            queue = [(x,y)]
            while queue:
                currx,curry = queue.pop(0)
                if currx<0 or currx>=m or curry<0 or curry>=n:
                    continue
                if grid[currx][curry] == '0':
                    continue
                grid[currx][curry] = '0'
                queue.append((currx+1,curry))
                queue.append((currx-1,curry))
                queue.append((currx,curry+1))
                queue.append((currx,curry-1))
            return
            
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i,j)
                    count += 1
        return count
        
        
        
        '''
        dfs - ac
        '''
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
       
        def dfs(x,y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if grid[x][y] == '0':
                return
            grid[x][y] = '0'
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            return
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        return count
