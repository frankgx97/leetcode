import math
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        bfs - tle
        test cases:
        1. with backtrack: ["hot","dot","dog","lot","log","cog","dag","dap","iap"]
        2. no solution: ["hat","qat","qay"]
        3. no transformation: "hit", "hig", []
        3. end word not in the list "hit", "hig", ["hip"]
        4. end word not in the list "hit", "hap", ["hip"]
        5. "hot","dog",["hot","dog","dot"]
        
        another bfs approach: https://www.cnblogs.com/zuoyuan/p/3765858.html
        '''
        def diff(a,b):
            d = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    d+=1
            return d

        queue = [beginWord]
        visited = set()
        counter = len(queue)
        ladder = 0
        while len(queue) > 0:
            current = queue.pop(0)
            visited.add(current)
            
            counter -= 1
            if counter <= 0:
                counter = len(queue)+1
                ladder+=1
                    
            if current == endWord:
                return ladder
            
            for i in range(len(wordList)):
                if diff(current, wordList[i]) == 1 and wordList[i] not in visited:
                    queue.append(wordList[i])
        return 0
