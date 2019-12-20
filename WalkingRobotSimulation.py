class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        '''
        simulation - ac
        use two array to represent facing and direction
        '''
        # (0,1) north
        # (-1,0) west
        # (0,-1) south
        # (1,0) east
        facex = [0,-1,0,1]
        facey = [1,0,-1,0]
        facing = 0# north
        currx = 0
        curry = 0
        ans = 0
        obs = set(map(tuple, obstacles))
        #+1 to turn left, -1 to turn right
        for i in commands:
            if i == -2:
                facing = (facing+1)%4
            elif i == -1:
                facing = (facing-1)%4
            elif 1<=i<=9:
                for j in range(i):
                    if (currx+facex[facing],curry+facey[facing]) not in obs:
                        currx+=facex[facing]
                        curry+=facey[facing]
                        ans = max(ans, abs(currx)**2 + abs(curry)**2)
                    else:
                        break
        return ans
