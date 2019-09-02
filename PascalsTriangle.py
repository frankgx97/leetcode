class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range(0,numRows):
            tri.append([1]*(i+1))
            if i < 2:
                    continue
            for j in range(1,len(tri[i])-1):
                tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
        return tri            
