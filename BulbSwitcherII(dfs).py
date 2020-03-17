class Solution:
    def flipLights(self, n: int, m: int) -> int:
        '''
        dfs - tle
        '''
        def t1(status):
            for i in range(len(status)):
                status[i] = not status[i]
            return status
        
        def t2(status):
            for i in range(1,len(status),2):
                status[i] = not status[i]
            return status
        
        def t3(status):
            for i in range(0,len(status),2):
                status[i] = not status[i]
            return status
        
        def t4(status):
            for i in range(len(status)):
                if (i)%3 == 0:
                    status[i] = not status[i]
            return status
            
        s = []
        
        def dfs(status, index):
            if index == m:
                if status not in s:
                    s.append(status)
                return
            dfs(t1(status[:]),index+1)
            dfs(t2(status[:]),index+1)
            dfs(t3(status[:]),index+1)
            dfs(t4(status[:]),index+1)
            return 
        
        
        dfs([True]*n,0)
        return len(s)
