class Solution:
    candidates = []
    results = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.candidates = nums
        self.dfs(0,[])
        return self.results

    def dfs(self, index, path):
        if len(path) > len(self.candidates):
            return
        self.results.append(path)
        for i in range(index, len(self.candidates)):
            self.dfs(i+1, path+[self.candidates[i]])
