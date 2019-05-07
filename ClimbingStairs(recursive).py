class Solution:
    def climbStairs(self, n: int) -> int:
       return self.dp(n)

    def dp(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.dp(n-1) + self.dp(n-2)
