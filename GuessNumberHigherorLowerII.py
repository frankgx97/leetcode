class Solution:
    def getMoneyAmount(self, n: int) -> int:
        '''
        recursive with memo
        ref: https://www.hrwhisper.me/leetcode-guess-number-higher-lower-ii/
        '''
        memo = {}
        def solve(l,r):
            if (l,r) in memo:
                return memo[(l,r)]
            if l >= r:
                return 0
            mi = float('inf')
            for i in range(l,r+1):
                curr = i + max(solve(l,i-1), solve(i+1,r))
                mi = min(mi,curr)
            memo[(l,r)] = mi
            return mi
        return solve(1,n)  
