class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: -x[0])
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
