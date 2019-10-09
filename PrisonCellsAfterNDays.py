class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N > 14:
            N = N%14
        if N%14 == 0:
            N = 14
        for i in range(N):
            temp = [0]*len(cells)
            for j in range(1,len(cells)-1):
                temp[0] = 0
                temp[len(cells)-1] = 0
                if cells[j+1] == cells[j-1]:
                    temp[j] = 1
                else:
                    temp[j] = 0
            cells = temp
        return cells
