class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = []
        for i in range(len(arr)-1):
            dp.append([0]*len(arr[0]))
        dp.append(arr[-1])
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[i])):
                dp[i][j] = min(dp[i+1][:j]+dp[i+1][j+1:]) + arr[i][j]
        return min(dp[0])
