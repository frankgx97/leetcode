class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(array):
            dup = []
            for i in array:
                if i == '.':
                    continue
                if i not in dup:
                    dup.append(i)
                else:
                    return False
            return True
        
        def checkbox(horizonal, vertical):
            arr = []
            for h in range(horizonal, horizonal + 3):
                for v in range(vertical, vertical + 3):
                    arr.append(board[h][v])
            return check(arr)
                
        
        # row
        for i in board:
            if not check(i):
                return False
        
        # column
        for i in range(9):
            arr = []
            for j in board:
                arr.append(j[i])
            if not check(arr):
                return False
        
        #box
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not checkbox(i,j):
                    return False
        
        return True
