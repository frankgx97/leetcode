class UF:
    def __init__(self, size):
        self.res = [i for i in range(size)]
        self.group = size
        self.size = [1] * size #optimize

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
'''
union find
ref: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/discuss/831616/Python-Simple-Union-Find
'''
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
       
        ans = 0
        ua = UF(n+1)
        ub = UF(n+1)
        type_edges = [[] for _ in range(4)]
        for e in edges:
            type_edges[e[0]].append(e)

        for e in type_edges[3]:
            px = ua.find(e[1])
            py = ua.find(e[2])
            
            if px != py:
                ans += 1
                ua.union(px,py)
                ub.union(px,py)
        for e in type_edges[2]:
            px = ua.find(e[1])
            py = ua.find(e[2])
            
            if px != py:
                ans += 1
                ua.union(px,py)
        for e in type_edges[1]:
            px = ub.find(e[1])
            py = ub.find(e[2])
            
            if px != py:
                ans += 1
                ub.union(px,py)
        x = ua.find(1)
        if any(x != ua.find(i) for i in range(1, n + 1)):
            return -1
            
        x = ub.find(1)
        if any(x != ub.find(i) for i in range(1, n + 1)):
            return -1

        return len(edges) - ans
