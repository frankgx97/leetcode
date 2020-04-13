class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        p = {0:[0]}
        n=1
        last = 0
        for i in nums:
            if i == 0:
                curr = last - 1
            else:
                curr = last + 1
            if curr not in p:
                p[curr] = [n]
            else:
                p[curr] += [n]
            n+=1
            last = curr
        
        mx = 0
        for i in p:
            mx = max(mx, max(p[i]) - min(p[i]))
        return mx
