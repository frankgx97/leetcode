class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(stack, s):
            if not s:
                return not stack
            i = s [0]
            if i == '(':
                return dfs(stack+[i], s[1:])
            elif i == ')':
                if not stack:
                    return False
                elif stack[-1] != '(':
                    return False
                else:
                    #stack.pop(-1)
                    return dfs(stack[:len(stack)-1], s[1:])
            elif i == '*':
                a = dfs(stack, '(' + s[1:])
                b = dfs(stack, ')' + s[1:])
                c = dfs(stack, s[1:])
                return a or b or c
        return dfs([],s)
                    
