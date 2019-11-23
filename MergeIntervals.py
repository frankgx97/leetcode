import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        heap sort - ac
        '''
        heap = []
        for i in intervals:
            heapq.heappush(heap,(i[0],i))
        r = []
        while heap:
            curr = heapq.heappop(heap)
            if not r or curr[0] > r[-1][1]:
                r.append(curr[1])
            elif curr[1][1] > r[-1][1]:
                r[-1] = [r[-1][0], curr[1][1]]
        return r
