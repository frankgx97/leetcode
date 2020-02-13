class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def dfs(i,j,visited):
            if i == j:
                return True
            visited.add(i)
            for x in graph[i]:
                if x in visited:
                    continue
                if dfs(x,j,visited):
                    return True
            return False
            
        graph = {}
        notequal = []
        for i in equations:
            if i[1:3] == '==':
                if i[0] not in graph:
                    graph[i[0]] = [i[-1]]
                else:
                    graph[i[0]] += i[-1]
                if i[-1] not in graph:
                    graph[i[-1]] = [i[0]]
                else:
                    graph[i[-1]] += i[0]
            elif i[1:3] == '!=':
                if i[0] == i[-1]:
                    return False
                else:
                    notequal.append(([i[0],i[-1]]))
                    if i[0] not in graph:
                        graph[i[0]] = []
                    if i[-1] not in graph:
                        graph[i[-1]] = []
                        
        for i,j in notequal:
            if dfs(i,j,set()):
                return False
        return True
