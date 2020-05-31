class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        g = graph
        graph = {}
        for i in range(len(g)):
            graph[i] = g[i]
        
        #red = 1, blue = -1
        colors = [0]*(len(graph.keys()))
        
        r = True
        
        def dfs(node, color):
            nonlocal r
            for i in graph[node]:
                if colors[i] == 0:
                    colors[i] = color
                    dfs(i,-color)
                if colors[i] == -color:
                    r = False
        for i in graph.keys():
            if colors[i] == 0:
                dfs(i, 1)
        return r
