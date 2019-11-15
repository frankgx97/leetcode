class Solution:
    '''
    dfs - ac
    all candidates are positive, so backtrack if path sum reaches beyond target
    ref: https://www.tamarous.com/leetcode-backtrace-problems/
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r = []
        def dfs(path):
            if sum(path) == target:
                path.sort()
                if path not in r:
                    r.append(path)
                return
            if not candidates or sum(path) > target:
                return
            for i in candidates:
                if sum(path+[i]) <= target:
                    dfs(path+[i])
        dfs([])
        return r
