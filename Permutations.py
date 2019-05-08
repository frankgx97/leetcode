class Solution:
    candidates = []
    results = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.candidates = nums
        self.dfs([],[])
        return self.results
        
    def dfs(self, index, path):
        if len(path) == len(self.candidates):
            self.results.append(path)
            return
        elif len(path) > len(self.candidates):
            return
        else:
            for i in range(0, len(self.candidates)):
                if i in index:
                    continue
                self.dfs(index+[i], path+[self.candidates[i]])
