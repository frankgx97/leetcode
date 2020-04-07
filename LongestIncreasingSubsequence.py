class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp
        '''
        if nums == []:
            return 0
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
                    
