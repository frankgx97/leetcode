class Solution:
    def checkRecord(self, n: int) -> int:
        '''
        dfs - tle
        '''
        r = 0
        def dfs(status,a,l,index):
            nonlocal r
            if a > 1 or l > 2:
                return
            if index == n:
                r += 1
                return

            dfs('',a+1,0,index+1)
            dfs('',a,0,index+1)
            dfs('',a,l+1,index+1)
        
        dfs('',0,0,0)
        return r
