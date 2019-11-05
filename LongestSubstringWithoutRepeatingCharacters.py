class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window(list) - ac
        maintain a sliding window(using a list), iterate through the string, if the current item is not in the window, append it to the window.
        if current item exist in the window, start poping from the left of the window, until meet the duplicated item with the current item(the duplicate one should be popped as well). then append the current item into the window.
        after each iteration, update the max length of the windows.
        '''

        ma = 0
        window = []
        for i in range(len(s)):
            if s[i] not in window:
                window.append(s[i])
            else:
                while len(window) != 0:
                    if window[0] != s[i]:
                        window.pop(0)
                        continue
                    if window[0] == s[i]:
                        window.pop(0)
                        break
                window.append(s[i])
            ma = max(ma,len(window))
        return ma
