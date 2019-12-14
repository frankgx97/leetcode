class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        dfs - tle
        '''
        r = False
        def dfs(w):
            nonlocal r
            if w == '':
                r = True
                return
            for i in wordDict:
                if w.startswith(i):
                    dfs(w[len(i):])
            return
        dfs(s)
        return r
