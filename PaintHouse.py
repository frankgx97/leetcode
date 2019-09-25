class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[0,0,0]]
        for i in range(0,len(costs)):
            if i < len(costs)-1:
                dp.append([0,0,0])
            dp[i] = [   min(dp[i-1][1], dp[i-1][2]) + costs[i][0],
                        min(dp[i-1][0], dp[i-1][2]) + costs[i][1],
                        min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
                    ]
        return min(dp[-1])
