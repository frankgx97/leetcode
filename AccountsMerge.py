'''
union find
time: nlogn
space: n
'''
class UF:
    def __init__(self, size):
        self.res = [i for i in range(size)]
        self.group = size
        self.size = [1] * size

    def find(self, child):
        if self.res[child] != child:
            self.res[child] = self.find(self.res[child])
        return self.res[child]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.size[pa] > self.size[pb]:
            pa, pb = pb, pa
        self.group -= 1
        self.res[pa] = pb
        self.size[pb] += self.size[pa]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        for i in range(len(accounts)):
            for j in range(i, len(accounts)):
                name_i = accounts[i][0]
                name_j = accounts[j][0]
                email_i = set(accounts[i][1:])
                email_j = set(accounts[j][1:])
                if name_i == name_j and email_i & email_j:#merge
                    uf.union(i,j)
        ans = []
        mapping = {}
        for i in range(len(accounts)):
            curr = uf.find(i)
            if curr not in mapping:
                mapping[curr] = [i]
            else:
                mapping[curr].append(i)
        for i in mapping:
            curr = [accounts[i][0]]
            email = set(accounts[i][1:])
            for j in mapping[i]:
                email = email | set(accounts[j][1:])
            ans.append(curr + sorted(list(email)))
        return ans
