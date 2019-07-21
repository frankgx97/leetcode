class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(array, target):
            if array == []:
                return (0,False)
            left = 0
            right = len(array)-1
            mid = 0
            while(left <= right):
                mid = (right - left)//2 + left
                if array[mid] < target:
                    left = mid + 1
                elif array[mid] > target:
                    right = mid - 1
                else:
                    return (mid,True)
            return (right, False)

        if matrix == []:
            return False
        lst = []
        for i in matrix:
            if i == []:
                break
            else:
                lst.append(i[0])
        vertical = binarySearch(lst, target)[0]
        print(vertical)
        return binarySearch(matrix[vertical], target)[1]
