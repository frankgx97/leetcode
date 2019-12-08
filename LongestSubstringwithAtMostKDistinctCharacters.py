class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        sliding window - ac
        maintain a window with a dictionary
        iterate the string, and add the current one to the window
        if current window not valid, pop from front of window
        '''
        window = ''
        ma = 0
        left = 0
        right = 0
        wind = {}
        for i in range(len(s)):
            if s[i] not in wind:
                wind[s[i]] = 1
            else:
                wind[s[i]] += 1
            right = i
            while len(wind) > k:
                if wind[s[left]] > 1:
                    wind[s[left]] -= 1
                else:
                    del(wind[s[left]])
                left += 1
            ma = max(ma, right-left+1)
        return ma
