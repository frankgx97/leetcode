import copy
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        '''
        bfs - ac
        '''
        def get_succ(board):
            l = []
            for i in board:
                l += i
            l.sort()
            l.pop(0)
            l.append(0)
            return tuple(l)
        
        def hashing(board):
            l = []
            for i in board:
                l += i
            return tuple(l)
        
        def swap(b,x1,y1,x2,y2):
            ret = copy.deepcopy(b)
            temp = ret[x1][y1]
            ret[x1][y1] = ret[x2][y2]
            ret[x2][y2] = temp
            return ret
        
        def get_pos0(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        return (i,j)
        m = len(board)
        n = len(board[0])
        visited = set()
        pos0 = get_pos0(board)
        queue = [(board,0,pos0[0],pos0[1])]
        moves = 0
        succ = get_succ(board)
        
        while queue:
            curr = queue.pop(0)
            currboard, currmove = curr[0], curr[1]
            currpos0x, currpos0y = curr[2], curr[3]
            currhashed = hashing(currboard)
            if currhashed == succ:
                return currmove
            visited.add(currhashed)
            
            if 0<=currpos0y-1<n:
                l = swap(currboard,currpos0x, currpos0y,currpos0x, currpos0y-1)
                if hashing(l) not in visited:
                    queue.append((l,currmove+1,currpos0x, currpos0y-1))

            if 0<=currpos0y+1<n:
                r = swap(currboard,currpos0x, currpos0y,currpos0x, currpos0y+1)
                if hashing(r) not in visited:
                    queue.append((r,currmove+1,currpos0x, currpos0y+1))
            
            if 0<=currpos0x-1<m:
                u = swap(currboard,currpos0x, currpos0y,currpos0x-1, currpos0y)
                if hashing(u) not in visited:
                    queue.append((u,currmove+1,currpos0x-1, currpos0y))
            
            if 0<=currpos0x+1<m:
                d = swap(currboard,currpos0x, currpos0y,currpos0x+1, currpos0y)
                if hashing(d) not in visited:
                    queue.append((d,currmove+1,currpos0x+1, currpos0y))
        return -1
