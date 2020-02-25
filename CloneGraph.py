"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        g = [None]*101
        ma = 0
        queue = [node]
        visited = set()
        while queue:
            curr = queue.pop(0)
            if curr.val in visited:
                continue
            else:
                visited.add(curr.val)
            childs = []
            for i in curr.neighbors:
                childs.append(i.val)
            g[curr.val] = childs
            ma = max(ma,curr.val)
            queue += curr.neighbors
        graph = [None]
        for i in range(1,ma+1):
            graph.append(Node(val=i))
        for i in range(1,ma+1):
            for j in g[i]:
                graph[i].neighbors.append(graph[j])
        return graph[1]
