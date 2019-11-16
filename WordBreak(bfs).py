class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        bfs - tle
        case with backtrack: 
        "aaaaaa"
        ["aaaa", "aaa"]
        '''
        q = [s]
        while q:
            s = q.pop(0)
            if s == "":
                return True
            for i in range(len(wordDict)):
                if s.startswith(wordDict[i]):
                    q.append(s[len(wordDict[i]):])
        return False
