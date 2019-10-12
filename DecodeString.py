class Solution:
    def decodeString(self, s: str) -> str:
        def is_int(num):
            if num in ['0','1','2','3','4','5','6','7','8','9']:
                return True
            else:
                return False

        nstack = []
        pstack = []
        r = ''
        digits = ''
        for i in range(len(s)):
            if is_int(s[i]):
                if s[i+1] == '[':
                    digits += s[i]
                    nstack.append(int(digits))
                    digits = ''
                else:
                    digits += s[i]
            elif s[i] == '[':
                pstack.append(s[i])
            elif s[i] == ']':
                temp = ''
                while len(pstack[-1]) > 0:
                    if pstack[-1] == '[':
                        pstack.pop(-1)
                        break
                    temp += pstack[-1]
                    pstack.pop(-1)
                temp = temp[::-1]*nstack[-1]
                nstack.pop(-1)
                for j in temp:
                    pstack.append(j)
            else:
                pstack.append(s[i])
        for i in pstack:
            r+=i
        return r
