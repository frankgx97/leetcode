class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        brute force - tle
        note that range() and slice are both closed on right side, we should use range(i,len(s)+1) for the j loop in order not to miss the last character in case of the longest substring without repeat is the string itself.
        '''
        def repeat(ss):
            dic = {}
            for i in ss:
                if i in dic:
                    return False
                else:
                    dic[i] = 0
            return True

        ma = 0
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                if repeat(s[i:j]):
                    if j-i > ma:
                        ma = j-i
        return ma
