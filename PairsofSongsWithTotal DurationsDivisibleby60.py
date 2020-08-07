class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        hashmap
        Time: n
        '''
        index = [0]*60
        ans = 0
        for i in time:
            t = i%60
            ans += index[(60-t)%60]
            index[t]+=1
        return ans
