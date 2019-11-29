class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        '''
        bfs - tle
        '''
        
        visited_bikes = set()
        bike_set = set()
        
        for i in bikes:
            bike_set.add((i[0],i[1]))

        r = 0
        
        def manhattan(p1,p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        def bfs(x,y):
            visited = set()
            queue = [(x,y)]
            while queue:
                #print(queue)
                curr = queue.pop(0)
                if curr[0] < 0 or curr[1] < 0 or curr[0] > 999 or curr[1] > 999 or curr in visited:
                    continue
                visited.add(curr)
                if curr in bike_set and curr not in visited_bikes:
                    visited_bikes.add(curr)
                    return curr
                queue.append((curr[0]+1,curr[1]))
                queue.append((curr[0],curr[1]+1))
                queue.append((curr[0]-1,curr[1]))
                queue.append((curr[0],curr[1]-1))
        
        for i in workers:
            r += manhattan((i[0],i[1]),bfs(i[0],i[1]))
        return r
