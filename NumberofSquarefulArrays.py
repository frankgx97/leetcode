import math
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        '''
        dfs permuation - tle
        calculate every permutation of the input array
        then determin if it is a perfect square
        ref: https://leetcode.com/problems/permutations-ii/
        '''
        def is_square(arr):
            for i in range(1,len(arr)):
                curr = math.sqrt(arr[i]+arr[i-1])
                if int(curr) != curr:
                    return False
            return True
        def dfs(visited,path):
            nonlocal r
            if len(path) == len(A):
                if is_square(path):
                    r += 1
                return
            for i in range(len(A)):
                if visited[i] or (i>=1 and A[i-1]==A[i] and visited[i-1]):
                    continue
                else:
                    temp = visited[:]
                    temp[i] = True
                    dfs(temp,path+[A[i]])
        r = 0
        A.sort()
        dfs([False]*len(A),[])
        return r
