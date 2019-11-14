import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        heap - ac
        use heap to sort the start time of each meeting
        then use a list to store all of the end time of each meeting rooms
        '''
        if not intervals:
            return 0
        
        heap = []
        for i in intervals:
            heapq.heappush(heap, (i[0],i))
        
        rooms = []
        while len(heap) > 0:
            current = heapq.heappop(heap)[1]
            if not rooms:
                rooms.append(current[1])
            else:
                flag = False
                for i in range(len(rooms)):
                    if rooms[i] <= current[0]:
                        #previous
                        flag = True
                        rooms[i] = current[1]
                        break
                if not flag:
                    rooms.append(current[1])
        return len(rooms)
