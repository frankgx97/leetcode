import heapq
class HitCounter:
    '''
    heap - ac
    list will also work, but worse time complexity when poping (0)
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = []
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        heapq.heappush(self.h,timestamp)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.h and self.h[0] <= timestamp - 300:
            heapq.heappop(self.h)
        return len(self.h)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
