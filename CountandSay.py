class Solution:
    def countAndSay(self, n: int) -> str:
        r = ['1']
        prev = list('1')

        for i in range(n-1):
            current = []
            temp = []
            while prev:
                if not temp or prev[0] == temp[-1]:
                    #next item same with temp
                    temp.append(prev.pop(0))
                else:
                    #next item not the same with last in temp
                    #clear temp
                    current += list(str(len(temp))+temp[0])
                    temp = []
                    temp.append(prev.pop(0))
            current += list(str(len(temp))+temp[0])
            prev = current
            r.append(copy.copy(current))
        return ''.join(r[-1])
