class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = x^y
        one = 0
        for i in bin(c):
            if i == '1':
                one += 1
        return one
