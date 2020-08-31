class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        '''
        greedy
        find out the last presense of the current letter
        '''
        last = {}
        for i in range(len(S)):
            last[S[i]] = i
        ans = []
        currentlast = 0
        lastans = -1
        for i in range(len(S)):
            currentlast = max(currentlast, last[S[i]])
            if i >= currentlast:
                if last[S[i]] <= currentlast:
                    ans.append(currentlast - lastans)
                    lastans = currentlast
        return ans
