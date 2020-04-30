class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        '''
        bitwise and
        if having different length, result is 0
        '''
        r = m
        if len(bin(m)) != len(bin(n)):
            return 0
        for i in range(m+1,n+1):
            r = r&i
        return r
