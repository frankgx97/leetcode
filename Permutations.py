class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        dfs - ac
        ref: https://www.youtube.com/watch?v=oCGMwvKUQ_I
        '''
        result = []
        def dfs(index, path):
            if len(path) == len(nums):
                result.append(path)
                return
            for i in range(len(nums)):
                if i in index:
                    continue
                dfs(index+[i],path+[nums[i]])
            return
        dfs([],[])
        return result
