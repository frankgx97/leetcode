import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidate,path,index,target,result):
            if sum(path) > target:
                return
            if sum(path) == target:
                if path not in result:
                    result.append(path)
            for i in range(index, len(candidate)):
                candidate_m = copy.copy(candidate)
                p = candidate_m.pop(i)
                dfs(candidate_m,path+[p],i, target, result)
        candidates.sort()
        result = []
        dfs(candidates, [], 0, target, result)
        return result
