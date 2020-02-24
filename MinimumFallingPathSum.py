import copy
class Solution:
    '''
    dp bottom up - ac
    '''
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        dp = copy.deepcopy(A)
        for i in range(len(dp)-1):
            for j in range(len(dp[i])):
                dp[i][j] = 0
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + A[i][j]
                elif j == len(dp[i])-1:
                    dp[i][j] = min(dp[i+1][j],dp[i+1][j-1]) + A[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1]) + A[i][j]
        return min(dp[0])
