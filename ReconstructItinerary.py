class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        dfs -ac
        
        first sort the list with the second item in per ticket
        then construct a graph
        perform dfs on the graph, remove the item after visiting it.
        
        backtrack case: [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        
        '''

        tickets.sort(key=lambda x:x[1])
        graph = {}
        for i in tickets:
            if i[0] not in graph:
                graph[i[0]] = [i[1]]
            else:
                graph[i[0]].append(i[1])
        r = []
        def dfs(start):
            if start not in graph or not graph[start]:
                r.append(start)
                return
            
            while start in graph and graph[start]:
                curr = graph[start].pop(0)
                dfs(curr)

            r.append(start)
        dfs('JFK')
        return r[::-1]
