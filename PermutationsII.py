class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        dfs backtracking - ac
        almost the same with Permutation I
        first sort the input array, and use a array to store if a index have benn visited.
        '''
        def dfs(index, path):
            if len(path) == len(nums):
                result.append(path)
                return
            for i in range(len(nums)):
                # check if current index is visited,
                # and if other index with same value have been visited 
                # to avoid duplication
                if index[i] or (i>=1 and nums[i-1]==nums[i] and index[i-1]):
                    continue
                else:
                    tempindex = index[:]
                    tempindex[i] = True
                    dfs(tempindex,path+[nums[i]])

        nums.sort()
        result = []
        dfs([False]*len(nums),[])
        return result
