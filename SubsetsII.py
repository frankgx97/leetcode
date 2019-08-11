class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(candidates, path, index):
            path.sort()
            if path not in result:
                result.append(path)
            i=0
            for i in range(index, len(candidates)):
                dfs(candidates, path+[candidates[i]], i+1)
        
        result = []
        dfs(nums, [], 0)
        return result
