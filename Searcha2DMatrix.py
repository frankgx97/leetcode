class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        two binary searches - ac
        first search on column, then search on column
        time O(logn)
        space constant
        '''
        def bs(matrix,target):
            left = 0
            right = len(matrix)-1
            while left <= right:
                mid = left+(right-left)//2
                if matrix[mid][0] == target:
                    return mid, True
                elif matrix[mid][0] < target:
                    left = mid+1
                else:
                    right = mid-1
            return right, False
        
        def bs2(arr,target):
            left = 0
            right = len(arr)-1
            while left<=right:
                mid = left+(right-left)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return False
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row, ret = bs(matrix,target)
        if ret:
            return True
        return bs2(matrix[row],target)
