class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        recursive dfs - tle
        in each recursion,
        if the string length >= 1, if the 1st char is not '0', remove the 1st char in the string and start another recursion
        if the string length >= 2, if the integer that the first two char forms is larger than 0 and less or equal than 26,
        remove the first 2 chars in the string and start another recursion
        '''
        r = 0
        def dfs(string):
            nonlocal r
            if len(string) == 0:
                r += 1
                return
            
            if len(string) >= 1:
                if string[0] != '0':
                    dfs(string[1:])
                else:
                    return
            if len(string) >= 2:
                if 0 < int(string[0:2]) <=26:
                    dfs(string[2:])
            return
        
        dfs(s)
        return r
