import heapq
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        '''
        heap sort - ac
        must calculate all work-bike combinations, then sort and start arranging from the least distance.
        Time: O(M * N log M * N )
        Space: O(M * N)
        '''
        heap = []
        r = [-1]*len(workers)
        
        for i, (wX, wY) in enumerate(workers):
            for j, (bX, bY) in enumerate(bikes):
                dist = abs(wX - bX) + abs(wY - bY)
                heapq.heappush(heap, (dist, i, j))

        occupied_w, occupied_b = set(),set()
        while heap:
            d,wk,bk = heapq.heappop(heap)
            if wk not in occupied_w and bk not in occupied_b:
                r[wk] = bk
                occupied_w.add(wk)
                occupied_b.add(bk)
        return r
