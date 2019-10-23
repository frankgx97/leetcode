class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals == []:
            return 0
        intervals = sorted(intervals,key=lambda x:x[0])
        last = [-1]
        for i in intervals:
            curr = False
            for j in range(len(last)):
                if i[0] >= last[j]:
                    last[j] = i[1]
                    curr = True
                    break
            if not curr:
                last.append(i[1])
        return len(last)
