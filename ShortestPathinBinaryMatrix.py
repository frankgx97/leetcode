class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        bfs - ac
        '''
        m = len(grid)
        n = len(grid[0])
        def bfs():
            queue = [(0,0,1)]
            visited = set()
            while queue:
                curr = queue.pop(0)
                x,y,l = curr[0],curr[1],curr[2]
                if (x,y) == (m-1,n-1):
                    return l
                if (x,y) in visited or grid[x][y] == 1:
                    continue
                visited.add((x,y))
                if 0<= x + 1 <m and grid[x+1][y] == 0:
                    queue.append((x+1,y,l+1))
                if 0<= y + 1 <n and grid[x][y+1] == 0:
                    queue.append((x,y+1,l+1))
                if 0<= x + 1 <m and 0<= y + 1 <n and grid[x+1][y+1] == 0:
                    queue.append((x+1,y+1,l+1))
                if 0<= x - 1 <m and 0<= y + 1 <n and grid[x-1][y+1] == 0:
                    queue.append((x-1,y+1,l+1))
                if 0<= x - 1 <m and grid[x-1][y] == 0:
                    queue.append((x-1,y,l+1))
                if 0<= x - 1 <m and 0<= y - 1 <n and grid[x-1][y-1] == 0:
                    queue.append((x-1,y-1,l+1))
                if 0<= y - 1 <n and grid[x][y-1] == 0:
                    queue.append((x,y-1,l+1))
                if 0<= x + 1 <m and 0<= y - 1 <n and grid[x+1][y-1] == 0:
                    queue.append((x+1,y-1,l+1))
            return -1
        return bfs()
                

