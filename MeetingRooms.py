class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        '''
        heap - ac
        use heap to sort the start time of each meeting
        '''
        if not intervals:
            return True
        
        heap = []
        for i in intervals:
            heapq.heappush(heap, (i[0],i))
        
        rooms = 0
        while len(heap) > 0:
            current = heapq.heappop(heap)[1]
            if rooms <= current[0]:
                rooms = current[1]
            else:
                return False
        return True
