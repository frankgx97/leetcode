class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palin(ss):
            if len(ss) == 0:
                return
            left = 0
            right = len(ss) - 1
            
            while left <= right:
                if ss[left] != ss[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True
              
        r = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                if is_palin(s[i:j]) and j-i+1 > len(r):
                    r = s[i:j]
        return r
