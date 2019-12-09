class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        '''
        dfs - ac
        search 8 directions, not 4!
        '''
        def aja_mine(x,y):
            r = 0
            for dx,dy in direc:
                if 0<=x+dx<m and 0<=y+dy<n and board[x+dx][y+dy] == 'M':
                    r+=1
            return r
                
        def dfs(x,y):
            if (x,y) in visited:
                return
            else:
                visited.add((x,y))
            if board[x][y] == 'E':
                curr = aja_mine(x,y)
                if curr == 0:
                    board[x][y] = 'B'
                    for dx,dy in direc:
                        if 0<=x+dx<m and 0<=y+dy<n and (x+dx,y+dy) not in visited and board[x+dx][y+dy] == 'E':
                            dfs(x+dx,y+dy)
                else:
                    board[x][y] = str(curr)
            return
                
        x,y = click[0],click[1]
        m,n = len(board), len(board[0])
        
        direc = [(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]
        
        visited = set()
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        elif board[x][y] == 'E':
            dfs(x,y)
        return board
