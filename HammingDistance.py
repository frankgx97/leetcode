class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        xb = bin(x)[2:]
        yb = bin(y)[2:]
        if len(xb)>=len(yb):
            yb = '0'*(len(xb)-len(yb))+yb
        else:
            xb = '0'*(len(yb)-len(xb))+xb
        for index in range(len(xb)):
            if xb[index] != yb[index]:
                distance += 1
        return distance
        
