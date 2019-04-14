class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        stack = []
        for i in range(0,len(s)//2):
            stack.append(s[i])
        if len(s)%2 == 1:
            s = s[len(s)//2+1:]
        else:
            s = s[len(s)//2:]
        for i in s:
            if i != stack[-1]:
                return False
            stack.pop()
        if len(stack)>0:
            return False
        return True
