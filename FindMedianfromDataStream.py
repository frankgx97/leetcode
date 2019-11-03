class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap,-num)
        elif num >= -self.max_heap[0]:
            heapq.heappush(self.min_heap,num)
        else:
            heapq.heappush(self.max_heap,-num)
        
        if len(self.min_heap) > len(self.max_heap):
            while len(self.min_heap) != len(self.max_heap):
                if len(self.min_heap)+1 == len(self.max_heap):
                    break
                curr = self.min_heap[0]
                heapq.heappush(self.max_heap,-curr)
                heapq.heappop(self.min_heap)
        elif len(self.min_heap) < len(self.max_heap):
            while len(self.min_heap)+1 != len(self.max_heap):
                if len(self.min_heap) == len(self.max_heap):
                    break
                curr = self.max_heap[0]
                heapq.heappush(self.min_heap,-curr)
                heapq.heappop(self.max_heap)
        return

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0]+self.min_heap[0])/2
        
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
