# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def search(topright, bottomleft):
            if topright.x < bottomleft.x or topright.y < bottomleft.y or not sea.hasShips(topright, bottomleft):
                return 0
            
            if topright.x == bottomleft.x and topright.y == bottomleft.y:
                return 1
            
            summ = 0
            midx, midy = (topright.x + bottomleft.x) // 2, (topright.y + bottomleft.y) // 2
            
            summ += search(Point(midx,midy), bottomleft)
            summ += search(topright, Point(midx+1,midy+1))
            summ += search(Point(midx, topright.y), Point(bottomleft.x, midy+1))
            summ += search(Point(topright.x, midy), Point(midx+1, bottomleft.y))

            return summ
        return search(topRight, bottomLeft)
