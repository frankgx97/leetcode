import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        backup = copy.deepcopy(matrix)
        print (backup)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][n-i-1] = backup[i][j]
