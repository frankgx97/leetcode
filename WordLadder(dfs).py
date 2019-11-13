import math
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        dfs - tle
        test cases:
        1. with backtrack: ["hot","dot","dog","lot","log","cog","dag","dap","iap"]
        2. no solution: ["hat","qat","qay"]
        3. no transformation: "hit", "hig", []
        3. end word not in the list "hit", "hig", ["hip"]
        4. end word not in the list "hit", "hap", ["hip"]
        '''
        def diff(a,b):
            d = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    d+=1
            return d

        result = []
        def dfs(path,candidates,dest):
            current = path[-1]
            if current == dest:
                result.append(path)
                return
            if len(candidates) == 0:
                return
            for i in range(len(candidates)):
                if diff(current,candidates[i]) == 1:
                    dfs(path+[candidates[i]], candidates[:i]+candidates[i+1:], dest)
        dfs([beginWord], wordList, endWord)
        if len(result) == 0:
            return 0
        mi = math.inf
        for i in result:
            mi = min(mi,len(i))
        return mi
