class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        '''
        set - ac
        time O(n)
        space O(n)
        '''
        p = [i for i in range(1,N+1)]
        dic = {}
        for i in trust:
            if i[0] not in dic:
                dic[i[0]] = [i[1]]
            else:
                dic[i[0]].append(i[1])
        people = set(p)
        trusted = set(p)
        trust = set()
        for i in dic:
            trust.add(i)
            trusted = trusted & set(dic[i])
        trust = people - trust
        if (trust & trusted) and len(trust & trusted) == 1:
            return list(trust & trusted)[0]
        else:
            return -1
