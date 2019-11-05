class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window(two pointers) - ac
        maintain a sliding window with two pointers, iterate through the string, if the current item is not in the window,  expand the window to the right by 1.
        if current item exist in the window, start poping from the left of the window, until meet the duplicated item with the current item(the duplicate one should be popped as well). then expand the window to the right by 1.
        after each iteration, update the max with (right - left) since by the end of  each iteration, the windows will always be expanded to the right, so it's not necessary to add 1 to (right - left) when calculating the length of the window.
        '''

        ma = 0
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] not in s[left:right]:
                right += 1
            else:
                while right - left + 1 != 0:
                    if s[left] != s[i]:
                        left += 1
                        continue
                    if s[left] == s[i]:
                        left += 1
                        break
                right += 1
            ma = max(ma,right - left)
        return ma
