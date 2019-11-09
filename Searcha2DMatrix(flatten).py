class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        flatten the matrix - ac
        cuz The first integer of each row is greater than the last integer of the previous row, all of the numbers in the matrix are sorted
        flatten thw matrix into a 1d array and perform a binary search
        '''
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        def bs(l,target):
            left = 0
            right = len(l)-1
            while left <= right:
                mid = (left + right) //2
                if l[mid] == target:
                    return mid  
                elif l[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return -1
        
        arr = []
        for i in matrix:
            arr += i
        if bs(arr,target) == -1:
            return False
        else:
            return True
