class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        dp = []
        m = len(matrix)
        n = len(matrix[0])
        
        for _ in range(m+1):
            dp.append([0]*(n+1))
        
        ma = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    ma = max(ma,dp[i][j])
        print(dp)
        return ma**2
