class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dic = {}
        for i in range(len(points)):
            distance = abs(points[i][0])*abs(points[i][0]) + abs(points[i][1])*abs(points[i][1])
            if distance not in dic.keys():
                dic[distance] = [i]
            else:
                dic[distance].append(i)
        l = sorted(list(dic.keys()))
        r = []
        for i in range(0,min(K,len(l))):
            for j in dic[l[i]]:
                r.append(points[j])
        return r[:K]
