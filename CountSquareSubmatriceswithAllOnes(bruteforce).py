class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def is_square(x,y,rad):
            if x + rad > m  or y + rad > n:
                return False
            for i in range(x, x+rad):
                for j in range(y, y+rad):
                    if matrix[i][j] == 0:
                        return False
            return True
            
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        r = 0
        for rad in range(1,min(m,n)+1):
            for i in range(m):
                for j in range(n):
                    curr = is_square(i,j,rad)
                    if curr:
                        r += 1
        return r
