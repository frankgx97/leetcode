import heapq
class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        greedy - ac
        use dic and heap to calc and sort the freq of each char
        in each iteration select the char with highest freq.
        '''
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        heap = []
        for i in dic.keys():
            heapq.heappush(heap,(-dic[i],i))

        length = 0
        mid = 0
        while len(heap) > 0:
            first = heapq.heappop(heap)
            if -first[0] >= 2:
                length += 1
                if -first[0] - 2 > 0:
                    heapq.heappush(heap,(-(-first[0]-2),first[1]))
            else:
                mid = 1
                break
        return length * 2 + mid
