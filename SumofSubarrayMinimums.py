class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        '''
        count subarrays - tle
        time: O(n^2)
        '''
        s = 0
        for right in range(1,len(A)+1):
            for left in range(0,right):
                s += min(A[left:right])
        return s
