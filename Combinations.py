class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(candidate, path, k):
            if len(path) == k:
                result.append(path)
            for i in range(len(candidate)):
                dfs(candidate[i+1:], path+[candidate[i]], k)

        result = []
        candidate = []
        for i in range(1,n+1):
            candidate.append(i)
        dfs(candidate, [], k)
        return result
