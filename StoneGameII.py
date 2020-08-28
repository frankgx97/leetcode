class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        '''
        dfs with memo
        ref: https://www.youtube.com/watch?v=e_FrC5xavwI
        time: ??
        space: n^2
        '''
        length = len(piles)
        memo = {}
        def dfs(index, m):
            if index >= length:
                return 0
            if (index, m) in memo:
                return memo[(index, m)]
            
            m = min(m,length) #in case 2*m exceed the pile length
            
            if index + 2*m >= length:
                r = sum(piles[index:])
                memo[(index, m)] = r
                return r
            
            curr = 0
            best = float('-inf')
            for x in range(1, 2*m+1):
                curr += piles[index + x - 1]
                best = max(best, curr - dfs(index + x, max(m, x)))
            memo[(index, m)] = best
            return best
        summ = sum(piles)
        return (summ + dfs(0, 1))//2
