class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:  
        '''
        straight forward - ac
        count the moves, and win state of X and O
        3 cases will lead to failure
        1. count_x < count_o or count_x > count_o + 1
        2. X and O both wins
        3. if O wins, count_x must == count_o
        4. if X wins, count_x must == count_o+1
        '''
        col = [0]*3
        row = [0]*3
        diag = 0
        rdiag = 0
        
        count_x = 0
        count_o = 0
        count_space = 0
        for i in range(len(board)):
            count_x += board[i].count('X')
            count_o += board[i].count('O')
            count_space += board[i].count(' ')
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    row[i]+=1
                    col[j]+=1
                    if i == j:
                        diag+=1
                    if i == 3-1-j:
                        rdiag += 1
                elif board[i][j] == 'O':
                    row[i]-=1
                    col[j]-=1
                    if i == j:
                        diag-=1
                    if i == 3-1-j:
                        rdiag -= 1
        x_win = 0
        o_win = 0
        for i in range(3):
            if col[i] == 3 or row[i] == 3:
                x_win += 1
            if col[i] == -3 or row[i] == -3:
                o_win += 1
            
        if diag == 3 or rdiag == 3:
            x_win += 1
        if diag == -3 or rdiag == -3:
            o_win += 1

        if count_x < count_o or count_x > count_o + 1:
            return False
        if o_win > 0:
            if x_win > 0:
                return False
            return count_o == count_x
        if count_x != count_o+1 and x_win > 0:
            return False
        
        return True
