class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        dp = []
        for i in range(m):
            dp.append([0]*n)
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j]:
                    dp[i][j] = min(dp[i-1][j] ,dp[i][j-1] , dp[i-1][j-1])+1
                else:
                    dp[i][j] = 0
        r = 0
        for i in dp:
            r += sum(i)
        return r
