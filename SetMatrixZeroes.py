class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[len(matrix)-1])
        
        x = []
        y = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    x += [i]
                    y += [j]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in x or j in y:
                    matrix[i][j] = 0
        return
