class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        ret = 0
        memo = {}
        def dfs(candidates, index, res):
            nonlocal ret
            if index == len(candidates):
                if res == S:
                    memo[(index,res)] = 1
                    ret += 1
                else:
                    memo[(index,res)] = 0
            if (index,res) not in memo:
                memo[(index,res)] = dfs(candidates, index+1, res+candidates[index]) + dfs(candidates, index+1, res-candidates[index])
            return memo[index,res]
        dfs(nums,0,0)
        return memo[(0,0)]
