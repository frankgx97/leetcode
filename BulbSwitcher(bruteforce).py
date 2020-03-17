class Solution:
    def bulbSwitch(self, n: int) -> int:
        '''
        brute force
        '''
        bulbs = [True]*(n+1)
        for i in range(2,n+1):
            for j in range(i,n+1,i):
                bulbs[j] = not bulbs[j]
        s = 0
        for i in bulbs[1:]:
            if i:
                s+=1
        return s
