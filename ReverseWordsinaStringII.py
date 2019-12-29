class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        reverse whole string then reverse each word - ac
        time: O(n)
        space: constant
        '''
        def rev(left,right):
            while left < right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
            return
        
        s.reverse()
        l = 0
        for i in range(len(s)):
            if s[i] == ' ':
                rev(l,i-1)
                l = i+1
        rev(l,len(s)-1)
        return
