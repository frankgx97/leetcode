class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        r = []
        for i in range(0, len(T)):
            r.append(self.go(T,i,i,0))
        return r
        
    def go(self, T, init, index, count):
        if index > len(T) - 1:
            if (len(T) - init) == count:
                return 0
            else:
                return count
        if T[index] > T[init]:
            return count
        return self.go(T, init, index+1, count+1)
