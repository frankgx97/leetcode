class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        tle
        '''
        memo = {}
        def match(t,p):
            if (t,p) in memo:
                return memo[(t,p)]
            if not p:
                memo[(t,p)] = not t
                return not t
            if not t:
                memo[(t,p)] = not p or set(p) == set('*')
                return not p or set(p) == set('*')
            if p[0] != '?' and p[0] != '*':
                if t[0] != p[0]:
                    memo[(t,p)] = False
                    return False
                else:
                    memo[(t,p)] = match(t[1:],p[1:])
                    return match(t[1:],p[1:])
            elif p[0] == '?':
                memo[(t,p)] = match(t[1:],p[1:])
                return match(t[1:],p[1:])
            elif p[0] == '*':
                r = False
                for i in range(0,len(t)+1):
                    r = r or match(t[i:], p[1:])
                memo[(t,p)] = r
                return r
        return match(s,p)
