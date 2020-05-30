class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        DAG bfs topology sort - ac
        ref: alien dictionary
        '''
        graph = {}
        indegree = [0]*numCourses
        
        for i in range(numCourses):
            graph[i] = []
        
        for c in prerequisites:
            j,i = tuple(c)
            graph[i].append(j)
            indegree[j] += 1
        
        q = []
        
        visited = set()
        
        count = numCourses
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                visited.add(i)
                count -= 1
        
        while q:
            subq = q[:]
            q = []
            for i in subq:
                for j in graph[i]:
                    if indegree[j] >= 1:
                        indegree[j] -= 1
                    if indegree[j] == 0 and j not in visited:
                        q.append(j)
                        visited.add(j)
                        count -= 1
        return count == 0
            
        
        #==============================================
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
