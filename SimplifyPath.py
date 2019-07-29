class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for i in path:
            if i == "":
                continue
            elif i == '.':
                continue
            elif i == '..':
                stack = stack[:-1]
            else:
                stack.append(i)
        if stack == []:
            return '/'
        else:
            result = ""
            for i in stack:
                result = result + '/' + i
            return result
