# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        '''
        binary search
        '''
        left = 0
        right = n
        while left <= right:
            mid = left + (right-left) // 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return 1
