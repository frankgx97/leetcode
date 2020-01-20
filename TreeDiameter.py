class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        '''
        dag topological sorting - ac
        time : O(n)
        '''
        def construct_graph(edges):
            graph = {}
            ind = [0]*(len(edges)+1)
            for i in range(len(edges)+1):
                graph[i] = []
                
            for i in edges:
                graph[i[0]].append(i[1])
                graph[i[1]].append(i[0])
                    
                ind[i[0]] += 1
                ind[i[1]] += 1
            return (graph,ind)
        
        
        graph, ind = construct_graph(edges)
        nodes = len(edges)+1
        queue = []
        for i in range(len(ind)):
            if ind[i] == 1:
                queue.append(i)
        radius = 0
        while nodes > 2:
            inner = queue[:]
            queue = []
            while inner:
                curr = inner.pop(0)
                ind[curr] -= 1
                nodes -= 1
                for i in graph[curr]:
                    ind[i] -= 1
                    if ind[i] == 1:
                        queue.append(i)
            radius += 1
        return radius * 2 + nodes-1
