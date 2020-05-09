class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xset = set()
        yset = set()
        for i in coordinates:
            xset.add(i[0])
            yset.add(i[1])
        
        if len(xset) == 1 or len(yset) == 1:
            return True
        if coordinates[-1][0] - coordinates[0][0] == 0:
            return False
        a = (coordinates[-1][1] - coordinates[0][1]) // (coordinates[-1][0] - coordinates[0][0])
        b = coordinates[0][1] - a * coordinates[0][0]
        for i in coordinates:
            if a * i[0] + b != i[1]:
                return False
        return True
