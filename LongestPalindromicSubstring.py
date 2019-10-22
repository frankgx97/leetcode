class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palin(mid,s):
            left = mid
            right = mid
            even_right = mid + 1
            longest = ''
            odd = True
            even = True
            while left >=0 and right < len(s):
                if not odd and not even:
                    break
                if even_right < len(s) and even:
                    if s[left] == s[even_right] and even_right+1-left > len(longest):
                        longest = s[left:even_right+1]
                    else:
                        even = False
                
                if s[left] == s[right] and odd:
                    if right+1-left > len(longest):
                        longest = s[left:right+1]
                else:
                    odd = False
                
                left -= 1
                right += 1
                even_right += 1
            return longest

              
        r = ''
        for i in range(len(s)):
            curr = is_palin(i,s)
            if len(curr) > len(r):
                r = curr
        return r
