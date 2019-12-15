class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        dp - ac
        '''
        if s == '':
            return False
        dp = [0]*len(s)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i] = 1
            else:
                for j in range(i+1):
                    if dp[j-1] and s[j:i+1] in wordDict:
                        dp[i] = 1
        if dp[-1]:
            return True
        return False
