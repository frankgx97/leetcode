import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        '''
        heap + greedy - ac
        use heap to select the two min numbers, and add the sum back to the heap.
        '''
        su = 0
        heap = []
        for i in sticks:
            heapq.heappush(heap,i)
        while len(heap) > 1:
            x1 = heapq.heappop(heap)
            x2 = heapq.heappop(heap)
            su = su + x1 + x2
            heapq.heappush(heap,x1+x2)
        return su
