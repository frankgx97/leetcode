class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        dfs with memo - ac
        memorization ref https://leetcode.com/problems/word-break/discuss/384769/Python-DFS-solution-very-easy-to-understand.-44ms
        '''
        r = False
        def dfs(w):
            nonlocal r
            if w == '':
                r = True
                return
            if w in memo:
                return
            for i in wordDict:
                if w.startswith(i):
                    dfs(w[len(i):])
            memo.add(w)
            return
        
        memo = set()
        dfs(s)
        return r
