class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        split & reverse - ac
        time: O(n)
        sapce: O(n)
        '''
        s = s.split()
        left = 0
        right = len(s)-1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left+=1
            right-=1
        r = ''
        for i in s:
            r += i
            r += ' '
        r = r.rstrip()
        r = r.lstrip()
        return r
