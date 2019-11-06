class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        use a helper function to determin the longest palindrom starting from current character and expand to both sides.
        helper function accepts two parameters(midl and midr), if midl and midr are the same, it search for the odd cases; if they're different, it searches for the even cases.
        to avoid list index out of range, we do not perform a even search when reaching the last char in the string.
        '''
        def is_palin(s, midl, midr):
            l = midl
            r = midr
            while midl >= 0 and midr < len(s):
                if s[midl] != s[midr]:
                    return s[midl+1:midr]
                else:
                    midl -= 1
                    midr += 1
            return s[midl+1:midr]
  
        r = ''
        for i in range(len(s)):
            curr_odd = is_palin(s,i,i)
            if len(curr_odd) > len(r):
                r = curr_odd
            if i != len(s) -1:
                curr_even = is_palin(s,i,i+1)
                if len(curr_even) > len(r):
                    r = curr_even
        return r
