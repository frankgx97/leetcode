class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                r = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(r)
            elif i == '-':
                r =  int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(r)
            elif i == '*':
                r = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(r)
            elif i == '/':
                r = int(int(stack[-2]) / int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(r)
            else:
                stack.append(i)
        return stack[0]
