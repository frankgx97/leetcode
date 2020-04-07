class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        '''
        this is a follow up of 300. Longest Increasing Subsequence
        '''
        if nums == []:
            return 0
        dp = [1]*len(nums)
        c = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    #dp[i] = max(dp[i], dp[j]+1)
                    if dp[j] >= dp[i]:
                        dp[i] = dp[j]+1
                        c[i] = c[j]
                    elif dp[j] +1 == dp[i]:
                        c[i] += c[j]
                        
        #print(dp)
        #print(c)
        mx = max(dp)
        r = []
        for i in range(len(c)):
            if dp[i] == mx:
                r.append(c[i])
        return sum(r)
