class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dfs(array, alex, lee, curr):
            t = tuple([tuple(array), alex, lee, curr])
            if t in memo:
                return memo[t]
            
            if len(array) == 0:
                return alex > lee
            if curr == 0:#now alex
                ans = dfs(array[1:], alex+array[0], lee, 1) or dfs(array[:-2], alex+array[-1], lee, 1)
                memo[t] = ans
                return ans 
            else:
                ans = dfs(array[1:], alex, lee+array[0], 0) or dfs(array[:-2], alex, lee+array[-1], 0)
                memo[t] = ans
                return ans
                
        return dfs(piles, 0, 0, 0)
