import heapq
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        heap sort - ac
        split each line in to two parts
        identifier + data
        if current is letter-log, use "data+identifier" as the identifier for heap sorting(to handle tie case)
        '''
        letters = []
        digits = []
        for i in logs:
            br = i.split(' ',1)
            if br[1][0].isnumeric():
                #digit
                digits.append(i)
            else:
                #letter
                heapq.heappush(letters,(br[1]+br[0],i))
                
        r = []
        while letters:
            r.append(heapq.heappop(letters)[1])
        r += digits
        return r
