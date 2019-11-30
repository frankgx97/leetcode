class Solution:
    def tribonacci(self, n: int) -> int:
        def tib_recursive(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            return tib(n-1) + tib(n-2) + tib(n-3)
        
        def tib(n):
            s = [-1]*(n+1)
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            s[0],s[1],s[2] = 0,1,1
            
            for i in range(3,n+1):
                s[i] = s[i-1]+s[i-2]+s[i-3]
            return s[n]
        return tib(n)
