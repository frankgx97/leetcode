import copy
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        topological sort with bfs. - ac
        ref: course schedule, alien dictionary
        '''
        if n == 1:
            return [0]
        if n == 2:
            return [0,1]
        
        graph = {}
        ind = {}
                
        for i in range(0,n):
            graph[i] = []
            ind[i] = 0
            
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
            ind[i[1]] += 1
            ind[i[0]] += 1

        #bfs
        queue = []
        for i in ind.keys():
            if ind[i] == 1:
                queue.append(i)
        while queue:
            r = copy.copy(queue)
            for _ in range(len(r)):
                curr = queue.pop(0)
                #ind[curr] -= 1 #we don't need to -1 on ind[curr] because this item is not useful any more.
                for i in graph[curr]:
                    print(curr,i)
                    ind[i] -= 1
                    if ind[i] == 1:
                        queue.append(i)
        #return the last level of bfs.
        return r
