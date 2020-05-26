class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        '''
        kadane 
        ref: https://zhuanlan.zhihu.com/p/64455963
        '''

        ansmin, curmin = 1<<31, 0
        ansmax, curmax = -(1<<31), 0
        su = 0
        for a in A:
            curmax = max(curmax+a, a)
            ansmax = max(ansmax, curmax)
            curmin = min(curmin+a, a)
            ansmin = min(ansmin, curmin)
            su += a
        if ansmax < 0:
            return ansmax
        else:
            return max(ansmax, su - ansmin)
