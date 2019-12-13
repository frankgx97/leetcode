class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        '''
        dfs - tle
        corner case: remove empty string "" from candidates
        remove duplications in result array
        '''
        def dfs(w,ow,num):
            if len(w) == 0 and num>=2:
                r.add(ow)
            if len(w) == 0 and num<2:
                return
            for i in s:
                if w.startswith(i):
                    dfs(w[len(i):],ow,num+1)
            return
        
        s = set(words)
        if '' in s:
            s.remove('')
        r = set()
        for i in words:
            dfs(i,i,0)
        return list(r)
