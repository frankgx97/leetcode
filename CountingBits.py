class Solution:
    def countBits(self, num: int) -> List[int]:
        def toBinary(n):
            stack = []
            while n >= 0:
                if n == 0:
                    break
                else:
                    stack.append(n%2)
                    n = n//2
            return (stack[::-1])
        result = []
        for i in range(0, num+1):
            result.append(toBinary(i).count(1))
        return result
