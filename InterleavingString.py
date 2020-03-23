class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(s1,s2,s3):
            if (s1,s2,s3) in memo:
                return memo[(s1,s2,s3)]
            if len(s1) + len(s2) != len(s3):
                return False
            if s3 == '':
                return not (s1 and s2)
            if s1 and s1[0] == s3[0]:
                c1 =  dfs(s1[1:],s2,s3[1:])
            else:
                c1 = False
            if s2 and s2[0] == s3[0]:
                c2 = dfs(s1,s2[1:],s3[1:])
            else:
                c2 = False
            memo[(s1,s2,s3)] = c1 or c2
            return c1 or c2
        return dfs(s1,s2,s3)
