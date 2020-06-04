import heapq
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''
        greedy - sort by i[0]-i[1] 
        '''
        heap = []
        for i in costs:
            heapq.heappush(heap,(i[0]-i[1],i))
        n = 0
        r = 0
        while heap:
            if n < len(costs)//2:
                r += heapq.heappop(heap)[1][0]
            else:
                r += heapq.heappop(heap)[1][1]
            n += 1
        return r
