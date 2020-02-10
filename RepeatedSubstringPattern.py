class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        divide into several parts
        time: O(n^2)
        '''
        for part in range(2,len(s)+1):
            if len(s)%part != 0:
                continue
            else:
                div = len(s)//part
            pattern = s[0:div]
            for i in range(part):
                if s[i*div:i*div+div] != pattern:
                    break
            else:
                return True
        return False
