# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m,n = tuple(binaryMatrix.dimensions())
        r = 101
        x,y = 0,n-1
        while 0<=x<m and 0<=y<n:
            if binaryMatrix.get(x,y) == 0:
                x += 1
            elif binaryMatrix.get(x,y) == 1:
                r = min(r,y)
                y -= 1
        if r == 101:
            return -1
        else:
            return r
                
