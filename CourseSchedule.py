class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        DAG bfs topology sort - ac
        ref: alien dictionary
        '''
        graph = {}
        ind = [0]*numCourses
        for i in range(numCourses):
            graph[i] = []
        for i in prerequisites:
            graph[i[1]].append(i[0])
            ind[i[0]] += 1
        
        # bfs
        r = []
        queue = []
        for i in range(len(ind)):
            if ind[i] == 0:
                r.append(i)
                queue.append(i)
        while queue:
            curr = queue.pop(0)
            for i in graph[curr]:
                ind[i] -= 1
                if ind[i] == 0:
                    queue.append(i)
                    r.append(i)
        if len(r) != numCourses:
            return False
        else:
            return True
