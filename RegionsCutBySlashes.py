class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        '''
        dfs - ac
        represent each grid as a 3x3 matrix:
        backslash = [
            [0,0,1],
            [0,1,0],
            [1,0,0]
        ]
        slash = [
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ]
        then perform a dfs similar to number of islands
        '''
        def dfs(x,y):
            if not 0<=x<length*3 or not 0<=y<length*3 or g[x][y] != 0:
                return
            g[x][y] = 2
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)
            return
                
        def append_to(a,b):
            a[0] += b[0]
            a[1] += b[1]
            a[2] += b[2]
            return a
                                   
        length = len(grid)
        g = []
        backslash = [
            [0,0,1],
            [0,1,0],
            [1,0,0]
        ]
        slash = [
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ]       
        blank = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        for i in range(length):
            curr = [[],[],[]]
            for j in range(length):
                if grid[i][j] == '/':
                    curr = append_to(curr,backslash)
                elif grid[i][j] == '\\':
                    curr = append_to(curr,slash)
                else:
                    curr = append_to(curr,blank)
            for k in curr:
                g.append(k)
        count = 0
        for i in range(length*3):
            for j in range(length*3):
                if g[i][j] == 0:
                    dfs(i,j)
                    count += 1
        return count
        
