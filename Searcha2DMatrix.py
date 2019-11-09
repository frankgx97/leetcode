class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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
            return right
        
        first_col = []
        for i in matrix:
            first_col.append(i[0])
        row_no = bs(first_col,target)
        row = matrix[row_no]
        index = bs(row,target)
        if row[index] == target:
            return True
        else:
            return False
