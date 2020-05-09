class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        '''
        sliding window
        ref https://www.cnblogs.com/grandyang/p/12245317.html
        '''
        rst = su = left = 0
        n = len(A)
        for i in range(n):
            su += A[i]
            while left < i and su > S:
                su -= A[left]
                left += 1
            if su < S:
                continue
            if su == S:
                rst += 1
            j = left
            while j < i and A[j] == 0:
                rst += 1
                j+=1
        return rst
