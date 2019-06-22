import copy
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = copy.copy(matrix)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                dp[i][j] = 1 if dp[i][j] == '1' else 0

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        m = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m = max(m,dp[i][j])
        return m*m
        
