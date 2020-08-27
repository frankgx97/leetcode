class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        def dfs(index):
            if index >= len(stoneValue):
                return 0
            if index in memo:
                return memo[index]
            
            score = float('-inf')
            score = max(score, stoneValue[index] - dfs(index+1))
            if index + 1 < len(stoneValue):
                score = max(score, stoneValue[index] + stoneValue[index+1] - dfs(index+2))
            if index + 2 < len(stoneValue):
                score = max(score, stoneValue[index] + stoneValue[index+1] + stoneValue[index+2] - dfs(index+3))
            memo[index] = score
            return score
        r = dfs(0)
        if r < 0:
            return 'Bob'
        elif r > 0:
            return 'Alice'
        else:
            return "Tie"
