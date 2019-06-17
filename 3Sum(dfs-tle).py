class Solution:     
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, target, index):
            if len(path) > 3:
                return
            if len(path) == 3 and sum(path) == target:
                if sorted(path) not in duplicate:
                    duplicate.append(sorted(path))
                    result.append(path)
                return
            for i in range(index, len(nums)):
                dfs(path+[nums[i]], target, i+1)
        duplicate = []
        result = []
        dfs([], 0, 0)
        return result
