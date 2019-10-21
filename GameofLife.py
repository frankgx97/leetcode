import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height = len(board)
        width = len(board[0])
        def live_count(arr,x,y):
            count = 0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if (i==x and j == y) or i < 0 or i > height-1 or j < 0 or j > width-1:
                        continue
                    else:
                        if arr[i][j] == 1:
                            count += 1
            return count
        
        backup = copy.deepcopy(board)
        for i in range(0,height):
            for j in range(0,width):
                curr = live_count(backup,i,j)
                if board[i][j] == 1:
                    if curr < 2:
                        board[i][j] = 0
                    elif curr>3:
                        board[i][j] = 0
                else:
                    if curr == 3:
                        board[i][j] = 1
        return board
