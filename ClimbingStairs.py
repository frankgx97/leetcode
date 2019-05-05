class Solution:
    result = 0
    choices = [1,2]
    def climbStairs(self, n: int) -> int:
        self.dfs(n,list(),0)
        return self.result
        
    def dfs(self,target,path,index):
        if target < 0:
            return
        elif target == 0:
            self.result += 1
            return
        else:
            for i in range(0,len(self.choices)):
                self.dfs(target - self.choices[i], path + [self.choices[i]], i)
