class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        stack = [99999]
        for i in prices:
            if i >= stack[-1]:
                r = max(r, i - stack[-1])
            else:
                stack.append(i)
        return r
