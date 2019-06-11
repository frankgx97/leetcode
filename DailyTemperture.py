class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        r = [0]*len(T)
        stack = []
        for i in range(len(T)):
            while len(stack) > 0 and T[stack[-1]] < T[i]:
                r[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return r
