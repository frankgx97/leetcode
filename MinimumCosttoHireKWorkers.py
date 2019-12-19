import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        worker = []
        for i in range(len(quality)):
            worker.append((quality[i],wage[i],wage[i]/quality[i]))
        #sort with ratio -- why?
        worker.sort(key=lambda x:x[2])
        heap = []
        quality_sum = 0
        res = float('inf')
        '''
        use a max heap to maintain k workers with min quality
        we use max heap because we pop the max when heap length exceed k
        '''
        for i in worker:
            heapq.heappush(heap, (-i[0],i))
            quality_sum += i[0]
            if len(heap) > K:
                quality_sum -= -heapq.heappop(heap)[0]
            if len(heap) == K:
                res = min(res,i[2]*quality_sum)
        return res
