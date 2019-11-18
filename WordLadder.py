import math
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        bfs - ac
        test cases:
        1. with backtrack: ["hot","dot","dog","lot","log","cog","dag","dap","iap"]
        2. no solution: ["hat","qat","qay"]
        3. no transformation: "hit", "hig", []
        3. end word not in the list "hit", "hig", ["hip"]
        4. end word not in the list "hit", "hap", ["hip"]
        5. "hot","dog",["hot","dog","dot"]
        '''

        word_set = set(wordList)
        result = []
        queue = [beginWord]
        visited = set()
        ladder = 1
        while len(queue) > 0:
            for i in range(len(queue)):# current level
                current = queue.pop(0)
                visited.add(current)
                    
                if current == endWord:
                    return ladder
                
                for j in range(len(current)):
                    for k in range(0,26):
                        cur = current[:j] + chr(ord('a')+k) + current[j+1:]
                        if cur in word_set and cur not in visited and cur not in queue:
                            queue.append(cur)

            ladder += 1
        return 0
