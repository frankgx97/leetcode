class Solution:
    def calculate(self, s: str) -> int:
        def to_postfix(s):
            '''
            infix to postfix
            
            ref: http://www.cse.psu.edu/~kxc104/ee324/02f/hw472/hw7.html
            ref: https://leetcode.com/problems/basic-calculator-iii/discuss/414896/Infix-to-Postfix-a-general-approach-to-similar-questions
            
            cases with negative:
            "-1+4*3/3/3"
            "1 - (-7)"
            '''
            '''
            中缀表达式a + b*c + (d * e + f) * g，其转换成后缀表达式则为a b c * + d e * f  + g * +。

            转换过程需要用到栈，具体过程如下：
            1）如果遇到操作数，我们就直接将其输出。
            2）如果遇到操作符，则我们将其放入到栈中，遇到左括号时我们也将其放入栈中。
            3）如果遇到一个右括号，则将栈元素弹出，将弹出的操作符输出直到遇到左括号为止。注意，左括号只弹出并不输出。
            4）如果遇到任何其他的操作符，如（“+”， “*”，“（”）等，从栈中弹出元素直到遇到发现更低优先级的元素(或者栈为空)为止。弹出完这些元素后，才将遇到的操作符压入到栈中。有一点需要注意，只有在遇到" ) "的情况下我们才弹出" ( "，其他情况我们都不会弹出" ( "。
            5）如果我们读到了输入的末尾，则将栈中所有元素依次弹出。
            '''
            priority = {
                '+':0,
                '-':0,
                '*':1,
                '/':1,
                '^':2
            }
            stack = []
            r = []
            temp = ''
            prev = ''
            for i in s:
                #print(stack)
                if '0' <= i <= '9':
                    #r.append(i)
                    temp += i
                    prev = i
                elif i == '(':
                    if temp:
                        r.append(int(temp))
                        temp = ''
                    stack.append(i)
                    prev = i
                elif i == ')':
                    if temp:
                        r.append(int(temp))
                        temp = ''
                    #print(stack)
                    while stack[-1] != '(':
                        r.append(stack.pop(-1))
                    stack.pop(-1)
                    prev = i
                elif i in '+-*/':
                    if temp:
                        r.append(int(temp))
                        temp = ''
                    if (i == '-' or i == '+') and prev in ['', '(', '+', '-', '*', '/']:
                        # handle negative number
                        # if a '-' appear after a operator, or at the head of the expression
                        # it indicates a negative number
                        # use ^ to present negative in postfix exp
                        if i == '-':
                            stack.append('^')

                        continue
                    while stack and (stack[-1] != '(' and priority[i] <= priority[stack[-1]]):
                        r.append(stack.pop(-1))
                    stack.append(i)
                    prev = i
                
            if temp:
                r.append(int(temp))
                temp = ''
            while stack:
                r.append(stack.pop(-1))
            return r
        
        def calc(postfix):
            stack = []
            for i in postfix:
                if type(i) == int:
                    stack.append(i)
                else:
                    #negative number
                    if i == '^':
                        stack.append(-int(stack.pop(-1)))
                        continue
                    op2 = int(stack.pop(-1))
                    op1 = int(stack.pop(-1))
                    if i == '+':
                        stack.append(op1+op2)
                    elif i == '-':
                        stack.append(op1-op2)
                    elif i == '*':
                        stack.append(op1*op2)
                    elif i == '/':
                        stack.append(op1//op2)
            return stack[0]
        
        return calc(to_postfix(s))
