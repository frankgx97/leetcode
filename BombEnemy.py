class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        '''
        brute force - ac
        '''
        def explode(xx,yy):
            dead = set()
            r = 0
            #u
            x = xx
            y = yy
            while 0<=x<m:
                if grid[x][y] == 'E' and (x,y) not in dead:
                    r += 1
                    dead.add((x,y))
                if grid[x][y] == 'W':
                    break
                x -= 1
            #d
            x = xx
            y = yy
            while 0<=x<m:
                if grid[x][y] == 'E' and (x,y) not in dead:
                    r += 1
                    dead.add((x,y))
                if grid[x][y] == 'W':
                    break
                x += 1
            #l
            x = xx
            y = yy
            while 0<=y<n:
                if grid[x][y] == 'E' and (x,y) not in dead:
                    r += 1
                    dead.add((x,y))
                if grid[x][y] == 'W':
                    break
                y -= 1
            #r
            x = xx
            y = yy
            while 0<=y<n:
                if grid[x][y] == 'E' and (x,y) not in dead:
                    r += 1
                    dead.add((x,y))
                if grid[x][y] == 'W':
                    break
                y += 1
            return r
        
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res,explode(i,j))
        return res
