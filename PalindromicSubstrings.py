class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        expand from center - ac
        similar to "longest palindromic substring"
        '''
        def isp(s,l,r):
            c = 0
            while l>=0 and r<=len(s)-1:
                if s[l]==s[r]:
                    c+=1
                    l-=1
                    r+=1
                else:
                    break
            return c
        
        r = 0
        for i in range(len(s)):
            r += isp(s,i,i)
            if i!=len(s)-1:
                r+=isp(s,i,i+1)
        return r
