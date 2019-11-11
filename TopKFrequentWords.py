import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        heap - ac
        use dict to count and use heap to sort
        almost same with "most common word"
        '''
        words.sort()
        dic = {}
        for i in words:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        heap = []
        for i in dic.keys():
            heapq.heappush(heap,(-dic[i],i))
        r = []
        for i in range(k):
            r.append(heap[0][1])
            heapq.heappop(heap)
        return r
