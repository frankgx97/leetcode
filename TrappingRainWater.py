class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        dp = [-1]*len(height)
        dp2 = [-1]*len(height)
        r = []
        
        dp[0] = 0
        for i in range(1,len(height)):
            dp[i] = max(dp[i-1],height[i-1])
        
        dp2[len(dp2)-1] = 0
        for i in reversed(range(0,len(height)-1)):
            dp2[i] = max(dp2[i+1],height[i+1])
        
        for i in range(len(dp)):
            temp = min(dp[i],dp2[i]) - height[i]
            if temp < 0:
                temp = 0
            r.append(temp)
        return sum(r)
