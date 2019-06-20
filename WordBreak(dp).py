class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def d(s, word, index):
            r = True
            for i in range(1,len(word)+1):
                r = (word[-i] == s[index-i]) and r
            return r

        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for word in wordDict:
                dp[i] = dp[i] or (d(s, word, i) and dp[i-len(word)])
        return dp[-1]
