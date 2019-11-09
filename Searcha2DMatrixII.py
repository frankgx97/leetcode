class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        ac
        because both direction is mono increasing or decreasing, we start from the lower left, 
        if target is smaller than current, go upwards;
        if target is larger than current, go right;
        when reaching (beyond) the upper bound or right bound, the search fails
        '''
        
        '''
        [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]20
        '''
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        i = len(matrix) -1
        j = 0
        while i >= 0 and j <= len(matrix[0]) - 1:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                i-=1
            else:
                j+=1
        return False
