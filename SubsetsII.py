class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(candidates, path, index):
            if path not in result:
                result.append(path)
            for i in range(index, len(candidates)):
                dfs(candidates, path+[candidates[i]], i+1)
        
        nums.sort()
        result = []
        dfs(nums, [], 0)
        return result
