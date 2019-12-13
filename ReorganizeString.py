import heapq
class Solution:
    '''
    heap
    '''
    def reorganizeString(self, S: str) -> str:
        #max heap
        heap = []
        dic = {}
        for i in S:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in dic.keys():
            heapq.heappush(heap,(-dic[i], i))
                                #freq   , char
        r = ''
        while heap:
            currfreq, currchar = heapq.heappop(heap)
            currfreq = -currfreq
            if r == '' or r[-1] != currchar:
                r += currchar
                currfreq -= 1
                if currfreq > 0:
                    heapq.heappush(heap, (-currfreq, currchar))
            else:
                #duplication
                temp = (-currfreq,currchar)
                if len(heap) == 0:
                    return ""
                else:
                    currfreq, currchar = heapq.heappop(heap)
                    currfreq = -currfreq
                    r += currchar
                    currfreq -= 1
                    if currfreq > 0:
                        heapq.heappush(heap, (-currfreq, currchar))
                    heapq.heappush(heap, temp)

        if len(r) == len(S):
            return r
        else:
            return ''
