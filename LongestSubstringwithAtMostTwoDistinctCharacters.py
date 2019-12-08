class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        '''
        sliding window - ac
        iterate the string, and add the current one to the window
        if current window not valid, pop from front of window
        '''
        window = ''
        ma = 0
        for i in s:
            window += i
            while window and len(set(window)) > 2:
                window = window[1:]
            #print(window)
            ma = max(ma, len(window))
        return ma
