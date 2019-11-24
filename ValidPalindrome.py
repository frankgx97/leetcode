class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''
        for i in s:
            if 'a' <= i <= 'z' or '0' <= i <= '9':
                ns+=i
            elif 'A' <= i <= 'Z':
                ns+=i.lower()
        left = 0
        right = len(ns)-1
        while left<=right:
            if ns[left] != ns[right]:
                return False
            left += 1
            right -= 1
        return True
