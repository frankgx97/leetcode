class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        if circle exist in undirected graph
        dfs
        '''
        def add_to_graph(a,b):
            graph[a].append(b)
        
        def dfs(pred, node):
            visited.add(node)
            for i in graph[node]:
                if i != pred:
                    if i in visited:
                        return True
                    else:
                        if dfs(node, i):
                            return True
            return False
                
        
        graph = []
        for i in range(n):
            graph.append([])
        visited = set()
        for i in edges:
            add_to_graph(i[0], i[1])
            add_to_graph(i[1], i[0])
        
        if dfs(-1, 0):
            return False
        if len(visited) != n:
            return False
        return True
