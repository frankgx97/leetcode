class Solution:
    '''
    dfs - ac
    error in oj: Input [1, 100], why expected [[100]]
    corner case:
    9,9(no solution)
    0,0(expect[[]])
    '''
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        r = []
        candidates = [1,2,3,4,5,6,7,8,9]
        def dfs(path, index):
            if len(path) > k:
                return 
            if len(path) == k and sum(path) == n:
                r.append(path)
            for i in range(index,len(candidates)):
                if sum(path) + candidates[i] <= n:
                    dfs(path+[candidates[i]],i+1)
            return r
        
        dfs([],0)
        return r
