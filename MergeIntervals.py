class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        rst = []
        for i in intervals:
            if not rst or rst[-1][1] < i[0]:
                rst.append(i)
            else:
                rst[-1][1] = max(i[1],rst[-1][1])
        return rst
