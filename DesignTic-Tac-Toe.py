class TicTacToe:
    '''
    o(n) - ac
    use two lists col and row to store the state in each row and col.
    and diag for diagnal, rdiag for reverse diagonal
    after each move, add 1 for player1 (or -1 for player2) to the col and row of the move.
    if one item in col/row or diag or rdiag reach n, player1 win; if reach -n, player2 win.
    '''
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.d = []
        for i in range(n):
            self.d.append([0]*n)
        self.row = [0]*n
        self.col = [0]*n
        self.diag = 0
        self.rdiag = 0
        
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            if row == col:
                self.diag += 1
            if self.n-1-row == col:
                self.rdiag += 1
            self.col[col] += 1
            self.row[row] += 1
        elif player == 2:
            if row == col:
                self.diag -= 1
            if self.n-1-row == col:
                self.rdiag -= 1
            self.col[col] -= 1
            self.row[row] -= 1
        for i in self.col:
            if i == self.n:
                return 1
            elif i == -self.n:
                return 2
        for i in self.row:
            if i == self.n:
                return 1
            elif i == -self.n:
                return 2
        if self.diag == self.n or self.rdiag == self.n:
            return 1
        elif self.diag == -self.n or self.rdiag == -self.n:
            return 2
        print(self.row)
        return 0
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
