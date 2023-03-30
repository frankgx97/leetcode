'''
topological sorting
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        ind = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            ind[course] += 1
        
        q = []
        taken = set()

        for i in range(len(ind)):
            if ind[i] == 0:
                q.append(i)
                taken.add(i)
        while q:
            curr = q.pop(0)
            for succ in graph[curr]:
                ind[succ] -= 1
                if ind[succ] == 0:
                    q.append(succ)
                    taken.add(succ)
        return len(taken) == numCourses
