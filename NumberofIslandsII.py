class UF:
    def __init__(self, m,n):
        self.count = 0
        self.res = [-1 for _ in range(m*n)]
        size = m*n
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
        self.count -= 1
        self.res[pa] = pb
        self.size[pb] += self.size[pa]

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        lands = set()
        def add_land(x,y):
            def check(x,y):
                return 0 <= x < m and 0 <= y < n and (x,y) in lands
            def check_and_union(x1,y1,x2,y2):
                uf.union(x1 * n + y1,x2 * n + y2)
                return
            if (x,y) in lands:
                return uf.count
            lands.add((x,y))
            uf.count += 1
            uf.res[x * n + y] = x * n + y
            if check(x+1,y):
                check_and_union(x,y,x+1,y)
            if check(x-1,y):
                check_and_union(x,y,x-1,y)
            if check(x,y+1):
                check_and_union(x,y,x,y+1)
            if check(x,y-1):
                check_and_union(x,y,x,y-1)
            return uf.count
        
        ans = []
        uf = UF(m,n)
        for i,j in positions:
            ans.append(add_land(i,j))
        return ans
