import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        '''
        heap - ac
        time O(nlogn)
        space O(n)
        '''
        heap = []
        for i in points:
            curr_distance = math.sqrt(i[0]**2+i[1]**2)
            heapq.heappush(heap,(curr_distance,i))
        r = []
        for i in range(K):
            r.append(heapq.heappop(heap)[1])
        return r
