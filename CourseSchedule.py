class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        topology sort - find cycle in graph
        ref: https://www.youtube.com/watch?v=VvKwqfXri0I
        
        '''
        
        def dfs(node):
            # return true means there is a cycle
            
            # check if current node is in visiting, if yes, there is a cricle
            if visiting[node]:
                return True
            
            # if current node is visited, treat it as it does not have any outcome
            if visited[node]:
                return False
            
            
            visiting[node] = 1
            for i in dic[node]:
                if dfs(i):
                    return True
            # once finding current node "safe", remove it from "visiting"
            # and add it to "visited"
            visiting[node] = 0
            visited[node] = 1
            return False
        
        
        visiting = [0]*numCourses
        visited = [0]*numCourses
        
        dic = []
        for i in range(numCourses):
            dic.append([])
        for i in prerequisites:
            dic[i[1]].append(i[0])
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
