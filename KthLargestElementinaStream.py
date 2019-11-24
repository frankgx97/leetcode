import heapq
class KthLargest:
    '''
    heap - only keep n items in the heap
    if heap length >= k
    remove heaptop and push new item in to heap when new item > heaptop
    '''

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for i in nums:
            self.ad(i)

    def add(self, val: int) -> int:
        self.ad(val)
        return self.h[0]
    
    def ad(self, v):
        if len(self.h) < self.k:
            heapq.heappush(self.h,v)
        else:
            if v>self.h[0]:
                heapq.heappop(self.h)
                heapq.heappush(self.h,v)
                
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
