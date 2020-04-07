class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dfs with memo - tle
        memo = {}
        def dfs(prev, curr):
            if curr >= len(nums):
                return 0
            if (prev,curr) in memo:
                return memo[(prev,curr)]
            t = 0
            if nums[curr] > prev:
                t = dfs(nums[curr],curr+1) + 1
            nt = dfs(prev,curr+1)
            memo[(prev, curr)] = max(t,nt)
            return max(t,nt)
        return dfs(-999999,0)
