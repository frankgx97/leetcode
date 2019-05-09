class Solution:
    n = 0
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        result = []
        self.dfs(0,0,"",result)
        return result
        
    def dfs(self,l,r,path,result):
        if len(path) > self.n*2:
            return
        elif len(path) == self.n*2:
            result.append(path)
            return
        else:
            if l < self.n:
                self.dfs(l+1, r, path+'(', result)
            if r < l:
                self.dfs(l, r+1, path+')', result)
