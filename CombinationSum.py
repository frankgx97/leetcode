class Solution:
    '''
    https://www.tamarous.com/leetcode-backtrace-problems/
    '''
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res,0)
        return res

    def dfs(self, nums, target, index, path, res, depth):
        depth+=1
        depthstr = ''
        for i in range(0,depth):
            depthstr += '-'
        #print(depthstr,nums, target, index, path, res)
        if target < 0:
            #print(depthstr, 'target:', target, '<0','backtrack!')
            return  # backtracking
        if target == 0:
            res.append(path)
            #print(depthstr, 'solution found:', path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res, depth)
