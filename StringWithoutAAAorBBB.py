class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:

        def letter_sort(a,b):
            dic = {}
            dic[a] = []
            dic[b] = []
            if a > 0:
                dic[a].append('a')
            if b > 0:
                dic[b].append('b')

            arr = [a,b]
            arr.sort()
            arr.reverse()
            result = []
            for i in arr:
                if i >0:
                    r_item = dic[i][0]
                    dic[i].pop(0)
                    result.append(r_item)
            return result

        def rlast(letter):
            if len(r)<2:
                return True
            else:
                if r[-1] == r[-2] == letter:
                    return False
                else:
                    return True

        r = ''
        while A>0 or B>0:
            seq = letter_sort(A,B)
            if len(seq) == 0:
                break
            flg = False
            for i in range(len(seq)):
                if rlast(seq[i]):
                    r+=seq[i]
                    if seq[i] == 'a':
                        A-=1
                    elif seq[i] == 'b':
                        B-=1
                    break
                else:
                    if i == len(seq)-1:
                        flg = True
            if flg:
                break
        return r
