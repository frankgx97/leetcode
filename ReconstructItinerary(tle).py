class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x:x[1])
        tickets.sort(key=lambda x:x[0])
        r=[]
        def dfs(path,candidates):
            if len(candidates) == 0:
                #print(path)
                nonlocal r
                if len(r) == 0:
                    r = path
                return
            flag = False
            for i in range(len(candidates)):
                if candidates[i][0] == path[-1]:
                    flag = True
                    dfs(path+[candidates[i][1]],candidates[:i]+candidates[i+1:])
                    
            if not flag:
                return

        dfs(['JFK'],tickets)
        return r
